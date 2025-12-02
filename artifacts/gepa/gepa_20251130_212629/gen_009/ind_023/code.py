
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F minor
pm.key_signature.key = 'f'
pm.key_signature.mode = 'minor'

# Define time constants
BPM = 160
BEAT = 60.0 / BPM  # 0.375 seconds per beat
BAR = 4 * BEAT    # 1.5 seconds per bar
TOTAL_DURATION = 4 * BAR  # 6 seconds total

# Create instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # for drum kit

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drum_program)

pm.instruments.append(sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# ---------------------------
# 🥁 DRUMS: Bar 1 (0.0 - 1.5s)
# Kick on 1 and 3
# Snare on 2 and 4
# Hihat on every eighth

drum_notes = {
    'kick': [pretty_midi.note_number_to_name(36)],  # C1
    'snare': [pretty_midi.note_number_to_name(38)],  # D1
    'hihat': [pretty_midi.note_number_to_name(42)],  # F1
}

# Kick on 1 and 3
for beat in [0, 2]:
    time = beat * BEAT
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
for beat in [1, 3]:
    time = beat * BEAT
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

# Hihat on every eighth note
for i in range(8):
    time = i * BEAT / 2
    note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

# ---------------------------
# 🎹 PIANO: Bars 2–4
# 7th chords on 2 and 4
# Fm7 on beat 2, Bbm7 on beat 4

def add_chord(note, time, duration=0.5):
    velocities = [80, 75, 70, 65]  # randomize velocities
    for pitch in note:
        n = pretty_midi.Note(velocity=velocities.pop(), pitch=pitch, start=time, end=time + duration)
        piano.notes.append(n)

# Fm7 = F, Ab, C, Eb
Fm7 = [53, 57, 58, 60]  # F, Ab, Bb, C, Eb? Wait, Fm7 is F, Ab, C, Eb
Fm7 = [53, 60, 62, 64]  # F, C, Eb, Gb? Wait, standard Fm7: F, Ab, C, Eb
# F = 53, Ab = 60, C = 64, Eb = 67
Fm7 = [53, 60, 64, 67]

# Bbm7: Bb, D, F, Ab
Bbm7 = [57, 62, 67, 71]

# Bar 2: 2nd beat
add_chord(Fm7, 1 * BEAT)

# Bar 3: 2nd beat
add_chord(Fm7, 1 * BEAT + 2 * BEAT)

# Bar 4: 4th beat
add_chord(Bbm7, 3 * BEAT)

# ---------------------------
# 🎺 SAX: Bars 2–4
# 1 short motif: Fm scale with tension, left hanging at the end

def add_sax_note(note, time, duration=0.25, velocity=100):
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration)
    sax.notes.append(n)

# Bar 2: Start the motif
add_sax_note(57, 1 * BEAT)        # Gb (Fm scale)
add_sax_note(60, 1 * BEAT + 0.25) # A
add_sax_note(64, 1 * BEAT + 0.5)  # C
add_sax_note(62, 1 * BEAT + 0.75) # Bb

# Bar 3: Repeat
add_sax_note(57, 2 * BEAT)
add_sax_note(60, 2 * BEAT + 0.25)
add_sax_note(64, 2 * BEAT + 0.5)
add_sax_note(62, 2 * BEAT + 0.75)

# Bar 4: End on a note that doesn't resolve
add_sax_note(62, 3 * BEAT)  # Bb, hanging — like a question

# ---------------------------
# 🎸 BASS: Bars 2–4
# Walking line, chromatic approach to F

def add_bass_note(note, time, duration=0.25):
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + duration)
    bass.notes.append(n)

# Bar 2: Chromatic approach to F
add_bass_note(53, 1 * BEAT)        # F
add_bass_note(52, 1 * BEAT + 0.25) # E
add_bass_note(54, 1 * BEAT + 0.5)  # F#
add_bass_note(53, 1 * BEAT + 0.75) # F

# Bar 3: Chromatic approach to F again
add_bass_note(53, 2 * BEAT)
add_bass_note(52, 2 * BEAT + 0.25)
add_bass_note(54, 2 * BEAT + 0.5)
add_bass_note(53, 2 * BEAT + 0.75)

# Bar 4: Chromatic approach to F, but end on Eb for tension
add_bass_note(53, 3 * BEAT)
add_bass_note(52, 3 * BEAT + 0.25)
add_bass_note(54, 3 * BEAT + 0.5)
add_bass_note(60, 3 * BEAT + 0.75)  # Bb — tension, not resolution

# Save the MIDI file
pm.write("jazz_intro_fm.mid")
