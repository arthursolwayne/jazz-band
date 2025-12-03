
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMidi(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key is F minor (F, Gb, Ab, Bb, B, Db, Eb)
key = 'Fm'

# Define the time for each bar (160 BPM, 4/4 time)
bar_length = 6.0 / 4  # 1.5 seconds per bar
note_length = bar_length / 4  # 0.375 seconds per beat

# Function to convert note name to MIDI note number (Fm key)
def note_to_midi(note_name):
    note_map = {
        'F': 65, 'Gb': 66, 'Ab': 67, 'Bb': 68, 'B': 69, 'Db': 70, 'Eb': 71
    }
    return note_map[note_name]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grands')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# ----------------------
# Bar 1: Little Ray (Drums) - Set it up
# Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
# Dynamic contrast: softer in the first bar, building tension
# Bar starts at time 0.0

# Kick on 1 and 3 (beats 0 and 2 in the bar)
kick_notes = [36]  # MIDI note for kick
kick_velocity = 50  # mid-volume

kick_1 = pretty_midi.Note(velocity=kick_velocity, pitch=kick_notes[0], start=0.0, end=0.375)
kick_3 = pretty_midi.Note(velocity=kick_velocity, pitch=kick_notes[0], start=0.75, end=1.125)

# Snare on 2 and 4 (beats 1 and 3 in the bar)
snare_notes = [38]  # MIDI note for snare
snare_velocity = 80  # higher volume

snare_2 = pretty_midi.Note(velocity=snare_velocity, pitch=snare_notes[0], start=0.375, end=0.75)
snare_4 = pretty_midi.Note(velocity=snare_velocity, pitch=snare_notes[0], start=1.125, end=1.5)

# Hihat on every eighth
hihat_notes = [42]  # MIDI note for hihat
hihat_velocity = 60  # mid-volume

hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5]
for t in hihat_times:
    hihat = pretty_midi.Note(velocity=hihat_velocity, pitch=hihat_notes[0], start=t, end=t + 0.1875)
    drums.notes.append(hihat)

# Add kick and snare to drums
drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# ----------------------
# Bar 2: Everyone in. Start of the melody (Sax)
# Start with a short motif: F, Ab, Bb, Eb (Fm7 chord notes)
# Leave it hanging, then return to finish it

# Sax motif: F (65), Ab (67), Bb (68), Eb (71)
# Start on beat 1, end on beat 2, then silence until bar 4

# Note 1: F
note_f = pretty_midi.Note(velocity=100, pitch=note_to_midi('F'), start=1.5, end=1.875)
sax.notes.append(note_f)

# Note 2: Ab
note_ab = pretty_midi.Note(velocity=100, pitch=note_to_midi('Ab'), start=1.875, end=2.25)
sax.notes.append(note_ab)

# Silence until bar 4 (beat 1)

# ----------------------
# Bar 3: Bass and Piano accompany
# Bass: Walking bass line in Fm, roots and fifths with chromatic approaches
# Piano: Open voicings, resolve on last chord of the bar

# Bass line: F (65), Bb (68), Ab (67), D (62)
# Bar 2: F, Bb, Ab, D

# Bass notes:
bass_notes = [note_to_midi('F'), note_to_midi('Bb'), note_to_midi('Ab'), note_to_midi('D')]
bass_velocities = [80, 85, 90, 80]

# Time for bar 2:
start_time = 1.5
for i, (pitch, velocity) in enumerate(zip(bass_notes, bass_velocities)):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time + i * note_length, end=start_time + i * note_length + note_length)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, Bb, Db), but open voicings: F, Ab, Bb, Db
# Play on beat 2 and 4

# First chord: Fm7 (F, Ab, Bb, Db)
chord_notes = [note_to_midi('F'), note_to_midi('Ab'), note_to_midi('Bb'), note_to_midi('Db')]
velocity = 70
for pitch in chord_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=2.25, end=2.625)
    piano.notes.append(note)

# ----------------------
# Bar 4: Sax returns to finish the melody
# F, Ab, Bb, Eb again, but this time finish it

# Note 3: Bb
note_bb = pretty_midi.Note(velocity=100, pitch=note_to_midi('Bb'), start=2.625, end=2.875)
sax.notes.append(note_bb)

# Note 4: Eb
note_eb = pretty_midi.Note(velocity=100, pitch=note_to_midi('Eb'), start=2.875, end=3.0)
sax.notes.append(note_eb)

# ----------------------
# Add more piano and bass for bar 4
# Bar 4: Resolving chord to Eb7 (Fm to Eb7 in the key of Fm)
# Chord: Eb7 (Eb, Gb, Bb, Db)
chord_notes = [note_to_midi('Eb'), note_to_midi('Gb'), note_to_midi('Bb'), note_to_midi('Db')]
for pitch in chord_notes:
    note = pretty_midi.Note(velocity=70, pitch=pitch, start=3.0, end=3.375)
    piano.notes.append(note)

# Bass line for bar 4: Eb (69), Ab (67), Bb (68), F (65)
bass_notes = [note_to_midi('Eb'), note_to_midi('Ab'), note_to_midi('Bb'), note_to_midi('F')]
for i, (pitch, velocity) in enumerate(zip(bass_notes, [85, 90, 80, 85])):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=3.0 + i * note_length, end=3.0 + i * note_length + note_length)
    bass.notes.append(note)

# ----------------------
# Add final drum fill to close bar 4
# Snare on beat 3, kick on beat 4, hihat on eighths

# Kick on beat 4 (time 3.0 to 3.375)
kick_4 = pretty_midi.Note(velocity=50, pitch=36, start=3.375, end=3.75)
drums.notes.append(kick_4)

# Snare on beat 3 (time 3.0 to 3.375)
snare_3 = pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375)
drums.notes.append(snare_3)

# Hihat on eighths
hihat_times = [3.0, 3.375, 3.75, 4.125]
for t in hihat_times:
    hihat = pretty_midi.Note(velocity=60, pitch=42, start=t, end=t + 0.1875)
    drums.notes.append(hihat)

# Save the MIDI file
pm.write('dante_intro.mid')
print("MIDI file written as 'dante_intro.mid'")
