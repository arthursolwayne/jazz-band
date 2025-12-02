
import pretty_midi

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)
drums = pretty_midi.Instrument(program=drums_program)

pm.instruments = [drums, bass, piano, sax]

# Constants for timing
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR = 4 * BEAT  # 4 beats per bar

# **Bar 1: Drums only — syncopated groove**
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0, end=BEAT))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2 * BEAT, end=3 * BEAT))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1 * BEAT, end=2 * BEAT))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3 * BEAT, end=4 * BEAT))

# Hi-hat on every eighth note
for i in range(0, 8):
    start_time = i * (BEAT / 2)
    end_time = start_time + (BEAT / 2)
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=end_time))

# **Bar 2: Bass line (walking in Fm with chromatic approach)**
# Fm: F, Ab, D, C (chords), but bass line is chromatic with Fm scale

# F, Gb (Ab), G, Ab, A, Bb (B), B, C, D, Eb, D, C
bass_notes = [71, 70, 71, 70, 72, 71, 72, 71, 72, 71, 72, 71]

for i, note in enumerate(bass_notes):
    start = (i) * (BEAT / 4)
    end = start + (BEAT / 4)
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start + BAR, end=end + BAR))

# **Bar 2: Piano comping (7th chords on 2 and 4)**
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab
# C7 = C, E, G, Bb
# D7 = D, F, A, C

# Bar 2: 2 and 4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1 * BEAT + BAR, end=1.25 * BEAT + BAR))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=1 * BEAT + BAR, end=1.25 * BEAT + BAR))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=1 * BEAT + BAR, end=1.25 * BEAT + BAR))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=1 * BEAT + BAR, end=1.25 * BEAT + BAR))  # Eb

# Bar 3: 2 and 4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3 * BEAT + BAR, end=3.25 * BEAT + BAR))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3 * BEAT + BAR, end=3.25 * BEAT + BAR))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3 * BEAT + BAR, end=3.25 * BEAT + BAR))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=3 * BEAT + BAR, end=3.25 * BEAT + BAR))  # Ab

# **Bar 2–4: Sax melody — fragmented motif with space and tension**

# Motif: F (beat 1), Ab (beat 2), D (beat 3), rest (beat 4)
# Repeat at bar 3 with a half-note rest in between

# Bar 2
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=0 * BEAT + BAR, end=0.25 * BEAT + BAR))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1 * BEAT + BAR, end=1.25 * BEAT + BAR))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2 * BEAT + BAR, end=2.25 * BEAT + BAR))  # D

# Rest on beat 4 (end of bar 2)
# Bar 3: Half-note rest
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.5 * BEAT + BAR, end=3.5 * BEAT + BAR))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.5 * BEAT + BAR, end=3.75 * BEAT + BAR))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4 * BEAT + BAR, end=4.25 * BEAT + BAR))  # D

# Save the MIDI file
pm.write("jazz_intro_florence.mid")
