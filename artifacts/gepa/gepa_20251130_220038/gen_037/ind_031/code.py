
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375)
hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)

drums.notes.extend([kick_1, snare_1, hihat_1, hihat_2, hihat_3, hihat_4, kick_2])

# Bar 2: Sax enters with melody
# Dm: D, F, G, A, Bb, C, C#, Eb, F, G, A, Bb
# Whisper -> cry

note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)  # D
note_2 = pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25) # F
note_3 = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625) # G
note_4 = pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)  # A

sax.notes.extend([note_1, note_2, note_3, note_4])

# Bass: Walking line in Dm
# D -> Eb -> F -> G -> A -> Bb -> C -> D

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),  # G
]

bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 (Bar 2: 2nd beat and 4th beat)
# Dm7: D, F, A, C

chord_1 = pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25) # D
chord_2 = pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25) # F
chord_3 = pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25) # A
chord_4 = pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25) # C

chord_5 = pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375) # D
chord_6 = pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375) # F
chord_7 = pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375) # A
chord_8 = pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375) # C

piano.notes.extend([chord_1, chord_2, chord_3, chord_4, chord_5, chord_6, chord_7, chord_8])

# Bar 3: Continue sax melody, build tension

note_5 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375) # Bb
note_6 = pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75) # C
note_7 = pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125) # G
note_8 = pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5)  # A

sax.notes.extend([note_5, note_6, note_7, note_8])

# Bass: Continue walking line

bass_notes_2 = [
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # A
]

bass.notes.extend(bass_notes_2)

# Piano: Comp on 2 and 4 again
# Dm7 again on beat 2 and 4 of Bar 3

chord_9 = pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75) # D
chord_10 = pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75) # F
chord_11 = pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75) # A
chord_12 = pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75) # C

chord_13 = pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875) # D
chord_14 = pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875) # F
chord_15 = pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875) # A
chord_16 = pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875) # C

piano.notes.extend([chord_9, chord_10, chord_11, chord_12, chord_13, chord_14, chord_15, chord_16])

# Bar 4: Sax resolves, plays final note

note_9 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875) # D

sax.notes.append(note_9)

# Bass: Final note of walking line

bass_notes_3 = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875), # D
]

bass.notes.extend(bass_notes_3)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
hihat_5 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375)
hihat_6 = pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75)
hihat_7 = pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125)
hihat_8 = pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
kick_4 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
snare_3 = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)
hihat_9 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875)

drums.notes.extend([kick_3, snare_2, hihat_5, hihat_6, hihat_7, hihat_8, kick_4, snare_3, hihat_9])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
