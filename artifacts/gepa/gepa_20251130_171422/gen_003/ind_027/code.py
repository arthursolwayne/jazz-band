
import pretty_midi

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature track
time_signature = pretty_midi.TimeSignature(4, 4, 0)
midi.time_signature_changes = [time_signature]

# Create instrument tracks
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
drums = pretty_midi.Instrument(program=drums_program)

bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
piano = pretty_midi.Instrument(program=piano_program)

sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Set beat duration (0.375s per beat at 160 BPM)
beat = 0.375

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, 4):
    # Kick on 1 and 3
    if i == 0 or i == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=i*beat, end=(i*beat)+beat/4)
        drums.notes.append(note)
    # Snare on 2 and 4
    if i == 1 or i == 3:
        note = pretty_midi.Note(velocity=110, pitch=38, start=i*beat, end=(i*beat)+beat/4)
        drums.notes.append(note)
    # Hihat on every eighth
    for j in range(0, 8):
        note = pretty_midi.Note(velocity=80, pitch=42, start=(i*beat)+(j*beat/4), end=(i*beat)+(j*beat/4)+beat/8)
        drums.notes.append(note)

# Bar 2: Bass enters with walking line in D
# D D# F A D D# F A (chromatic approach to F)
bass_notes = [2, 3, 5, 7, 2, 3, 5, 7]
for i in range(0, 8):
    pitch = 57 + bass_notes[i]  # D is 57
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=(i*beat)+beat, end=(i*beat)+beat+beat/4)
    bass.notes.append(note)

# Bar 2: Piano enters with 7th chords on 2 and 4
# D7 on 2: D F A C
# G7 on 4: G B D F
piano_notes = []
# D7 on beat 2
for pitch in [2, 5, 7, 10]:
    note = pretty_midi.Note(velocity=95, pitch=57 + pitch, start=beat*2, end=beat*2+beat/4)
    piano_notes.append(note)
# G7 on beat 4
for pitch in [7, 10, 12, 15]:
    note = pretty_midi.Note(velocity=95, pitch=67 + pitch, start=beat*4, end=beat*4+beat/4)
    piano_notes.append(note)
piano.notes.extend(piano_notes)

# Bar 2: Sax enters with motif
# D (57), E (58), F# (60), D (57)
sax_notes = [57, 58, 60, 57]
for i in range(0, 4):
    note = pretty_midi.Note(velocity=105, pitch=sax_notes[i], start=(i*beat)+beat, end=(i*beat)+beat+beat/4)
    sax.notes.append(note)

# Bar 3: Bass continues walking line
bass_notes = [2, 3, 5, 7, 2, 3, 5, 7]
for i in range(0, 8):
    pitch = 57 + bass_notes[i]
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=(i*beat)+beat*2, end=(i*beat)+beat*2+beat/4)
    bass.notes.append(note)

# Bar 3: Piano continues with 7th chords on 2 and 4
# A7 on 2: A C# E G
# D7 on 4: D F A C
piano_notes = []
# A7 on beat 2
for pitch in [2, 5, 7, 10]:
    note = pretty_midi.Note(velocity=95, pitch=65 + pitch, start=beat*2+beat*2, end=beat*2+beat*2+beat/4)
    piano_notes.append(note)
# D7 on beat 4
for pitch in [2, 5, 7, 10]:
    note = pretty_midi.Note(velocity=95, pitch=57 + pitch, start=beat*4+beat*2, end=beat*4+beat*2+beat/4)
    piano_notes.append(note)
piano.notes.extend(piano_notes)

# Bar 3: Sax continues motif
# D (57), E (58), F# (60), D (57)
sax_notes = [57, 58, 60, 57]
for i in range(0, 4):
    note = pretty_midi.Note(velocity=105, pitch=sax_notes[i], start=(i*beat)+beat*2, end=(i*beat)+beat*2+beat/4)
    sax.notes.append(note)

# Bar 4: Bass continues walking line
bass_notes = [2, 3, 5, 7, 2, 3, 5, 7]
for i in range(0, 8):
    pitch = 57 + bass_notes[i]
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=(i*beat)+beat*3, end=(i*beat)+beat*3+beat/4)
    bass.notes.append(note)

# Bar 4: Piano continues with 7th chords on 2 and 4
# B7 on 2: B D# F# A
# E7 on 4: E G B D
piano_notes = []
# B7 on beat 2
for pitch in [2, 5, 7, 10]:
    note = pretty_midi.Note(velocity=95, pitch=71 + pitch, start=beat*2+beat*3, end=beat*2+beat*3+beat/4)
    piano_notes.append(note)
# E7 on beat 4
for pitch in [2, 5, 7, 10]:
    note = pretty_midi.Note(velocity=95, pitch=64 + pitch, start=beat*4+beat*3, end=beat*4+beat*3+beat/4)
    piano_notes.append(note)
piano.notes.extend(piano_notes)

# Bar 4: Sax finishes the motif
# D (57), E (58), F# (60), D (57)
sax_notes = [57, 58, 60, 57]
for i in range(0, 4):
    note = pretty_midi.Note(velocity=105, pitch=sax_notes[i], start=(i*beat)+beat*3, end=(i*beat)+beat*3+beat/4)
    sax.notes.append(note)

# Write the MIDI file
midi.write('dante_intro.mid')
