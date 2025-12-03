
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.key_signature_changes = [pretty_midi.KeySignature(-3, 0)]  # F minor

# Time per bar (1.5 seconds)
bar_duration = 1.5
time_per_beat = bar_duration / 4  # 0.375 seconds per beat

# Create instruments
bass_program = Program(33)  # Electric Bass
piano_program = Program(0)   # Acoustic Piano
sax_program = Program(64)    # Tenor Saxophone
drums_program = Program(128) # Drums

# Bass instrument
bass = Instrument(program=bass_program)
pm.instruments.append(bass)

# Piano instrument
piano = Instrument(program=piano_program)
pm.instruments.append(piano)

# Sax instrument
sax = Instrument(program=sax_program)
pm.instruments.append(sax)

# Drums instrument
drums = Instrument(program=drums_program)
pm.instruments.append(drums)

#------------------ DRUMS (Bar 1 - 4) ------------------

# Kick on 1 and 3, snare on 2 and 4, hi-hat on every 8th
def add_drums(start_time):
    # Kick on 1 and 3
    kick_notes = [Note(36, 100, start_time, start_time + 0.1),  # beat 1
                  Note(36, 100, start_time + bar_duration * 0.5, start_time + bar_duration * 0.5 + 0.1)]  # beat 3
    drums.notes.extend(kick_notes)

    # Snare on 2 and 4
    snare_notes = [Note(38, 100, start_time + bar_duration * 0.25, start_time + bar_duration * 0.25 + 0.1),  # beat 2
                   Note(38, 100, start_time + bar_duration * 0.75, start_time + bar_duration * 0.75 + 0.1)]  # beat 4
    drums.notes.extend(snare_notes)

    # Hi-hat on every 8th
    for i in range(8):
        time = start_time + (i * time_per_beat)
        Note(42, 80, time, time + 0.05)
    drums.notes.extend([Note(42, 80, time, time + 0.05) for time in [start_time + i * time_per_beat for i in range(8)]])

# Bar 1: Drums only
add_drums(0)

# Bar 2-4: Drums again
add_drums(bar_duration)
add_drums(2 * bar_duration)
add_drums(3 * bar_duration)

#------------------ BASS (Bar 2 - 4) ------------------

# Bar 2: C (root) -> chromatic approach to F
note = Note(60, 80, bar_duration, bar_duration + 0.1)  # C
bass.notes.append(note)
note = Note(59, 80, bar_duration + 0.25, bar_duration + 0.25 + 0.1)  # Bb (chromatic to F)
bass.notes.append(note)
note = Note(60, 80, bar_duration + 0.5, bar_duration + 0.5 + 0.1)  # C
bass.notes.append(note)
note = Note(61, 80, bar_duration + 0.75, bar_duration + 0.75 + 0.1)  # C#
bass.notes.append(note)

# Bar 3: G -> chromatic approach to F
note = Note(67, 80, 2 * bar_duration, 2 * bar_duration + 0.1)  # G
bass.notes.append(note)
note = Note(66, 80, 2 * bar_duration + 0.25, 2 * bar_duration + 0.25 + 0.1)  # F#
bass.notes.append(note)
note = Note(67, 80, 2 * bar_duration + 0.5, 2 * bar_duration + 0.5 + 0.1)  # G
bass.notes.append(note)
note = Note(68, 80, 2 * bar_duration + 0.75, 2 * bar_duration + 0.75 + 0.1)  # G#
bass.notes.append(note)

# Bar 4: F (root)
note = Note(65, 80, 3 * bar_duration, 3 * bar_duration + 0.1)  # F
bass.notes.append(note)

#------------------ PIANO (Bar 2 - 4) ------------------

# Bar 2: Cm7 (C, Eb, G, Bb)
note = Note(60, 100, bar_duration, bar_duration + 0.25)  # C
piano.notes.append(note)
note = Note(63, 100, bar_duration, bar_duration + 0.25)  # Eb
piano.notes.append(note)
note = Note(67, 100, bar_duration, bar_duration + 0.25)  # G
piano.notes.append(note)
note = Note(67, 100, bar_duration, bar_duration + 0.25)  # Bb (62)
piano.notes.append(Note(62, 100, bar_duration, bar_duration + 0.25))

# Bar 3: Gm7 (G, Bb, D, F)
note = Note(67, 100, 2 * bar_duration, 2 * bar_duration + 0.25)  # G
piano.notes.append(note)
note = Note(62, 100, 2 * bar_duration, 2 * bar_duration + 0.25)  # Bb
piano.notes.append(note)
note = Note(65, 100, 2 * bar_duration, 2 * bar_duration + 0.25)  # D
piano.notes.append(note)
note = Note(65, 100, 2 * bar_duration, 2 * bar_duration + 0.25)  # F (65)
piano.notes.append(Note(65, 100, 2 * bar_duration, 2 * bar_duration + 0.25))

# Bar 4: Fm7 (F, Ab, C, Eb)
note = Note(65, 100, 3 * bar_duration, 3 * bar_duration + 0.25)  # F
piano.notes.append(note)
note = Note(66, 100, 3 * bar_duration, 3 * bar_duration + 0.25)  # Ab
piano.notes.append(note)
note = Note(60, 100, 3 * bar_duration, 3 * bar_duration + 0.25)  # C
piano.notes.append(note)
note = Note(63, 100, 3 * bar_duration, 3 * bar_duration + 0.25)  # Eb
piano.notes.append(note)

#------------------ SAX (Bar 2 - 4) ------------------

# Bar 2: F -> Ab -> Bb (start, leave it hanging)
note = Note(66, 100, bar_duration, bar_duration + 0.25)  # F
sax.notes.append(note)
note = Note(69, 100, bar_duration + 0.25, bar_duration + 0.5)  # Ab
sax.notes.append(note)
note = Note(71, 100, bar_duration + 0.5, bar_duration + 0.75)  # Bb
sax.notes.append(note)

# Bar 3: Repeat the motif, but resolve on Ab -> Bb
note = Note(66, 100, 2 * bar_duration, 2 * bar_duration + 0.25)  # F
sax.notes.append(note)
note = Note(69, 100, 2 * bar_duration + 0.25, 2 * bar_duration + 0.5)  # Ab
sax.notes.append(note)
note = Note(71, 100, 2 * bar_duration + 0.5, 2 * bar_duration + 0.75)  # Bb
sax.notes.append(note)

# Bar 4: End the motif with Bb, unresolved
note = Note(71, 100, 3 * bar_duration, 3 * bar_duration + 0.1)  # Bb
sax.notes.append(note)

#------------------ Save MIDI ------------------
pm.write('jazz_intro_in_fm.mid')
print("MIDI file 'jazz_intro_in_fm.mid' generated with 4-bar jazz intro.")
