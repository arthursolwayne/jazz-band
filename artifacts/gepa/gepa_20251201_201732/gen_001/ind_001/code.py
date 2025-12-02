
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_2 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375)
drum_3 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_4 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
drum_5 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drum_6 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_1, drum_2, drum_3, drum_4, drum_5, drum_6])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38)
bass_note_1 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)
bass_note_2 = pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25)  # F2 (chromatic approach)
bass_note_3 = pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625)  # E2 (chromatic approach)
bass_note_4 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4])

# Piano: F7 (MIDI 77) -> Bb7 (MIDI 79) -> G7 (MIDI 80) -> F7 (MIDI 77)
piano_note_1 = pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.0)
piano_note_2 = pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.5)
piano_note_3 = pretty_midi.Note(velocity=100, pitch=80, start=2.5, end=3.0)
piano.notes.extend([piano_note_1, piano_note_2, piano_note_3])

# Sax: motif - F (MIDI 65) -> G (MIDI 67) -> A (MIDI 69) -> F (MIDI 65)
sax_note_1 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875)
sax_note_2 = pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25)
sax_note_3 = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625)
sax_note_4 = pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0)
sax.notes.extend([sax_note_1, sax_note_2, sax_note_3, sax_note_4])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_7 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_8 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_9 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)
drum_10 = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
drum_11 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
drum_12 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)
drum_13 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
drums.notes.extend([drum_7, drum_8, drum_9, drum_10, drum_11, drum_12, drum_13])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 (MIDI 39) -> A2 (MIDI 42) -> G2 (MIDI 41) -> F2 (MIDI 39)
bass_note_5 = pretty_midi.Note(velocity=100, pitch=39, start=3.0, end=3.375)
bass_note_6 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)  # F2 chromatic approach
bass_note_7 = pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125)  # E2 chromatic approach
bass_note_8 = pretty_midi.Note(velocity=100, pitch=39, start=4.125, end=4.5)
bass.notes.extend([bass_note_5, bass_note_6, bass_note_7, bass_note_8])

# Piano: Bb7 (MIDI 79) -> G7 (MIDI 80) -> F7 (MIDI 77) -> C7 (MIDI 79)
piano_note_4 = pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.5)
piano_note_5 = pretty_midi.Note(velocity=100, pitch=80, start=3.5, end=4.0)
piano_note_6 = pretty_midi.Note(velocity=100, pitch=77, start=4.0, end=4.5)
piano.notes.extend([piano_note_4, piano_note_5, piano_note_6])

# Sax: motif variation - F (MIDI 65) -> G (MIDI 67) -> A (MIDI 69) -> Bb (MIDI 71)
sax_note_5 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375)
sax_note_6 = pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75)
sax_note_7 = pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125)
sax_note_8 = pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5)
sax.notes.extend([sax_note_5, sax_note_6, sax_note_7, sax_note_8])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_14 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_15 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drum_16 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)
drum_17 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
drum_18 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
drum_19 = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)
drum_20 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
drums.notes.extend([drum_14, drum_15, drum_16, drum_17, drum_18, drum_19, drum_20])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 (MIDI 39) -> A2 (MIDI 42) -> G2 (MIDI 41) -> C2 (MIDI 37)
bass_note_9 = pretty_midi.Note(velocity=100, pitch=39, start=4.5, end=4.875)
bass_note_10 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
bass_note_11 = pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625)
bass_note_12 = pretty_midi.Note(velocity=100, pitch=37, start=5.625, end=6.0)
bass.notes.extend([bass_note_9, bass_note_10, bass_note_11, bass_note_12])

# Piano: F7 (MIDI 77) -> Bb7 (MIDI 79) -> G7 (MIDI 80) -> F7 (MIDI 77)
piano_note_7 = pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=5.0)
piano_note_8 = pretty_midi.Note(velocity=100, pitch=79, start=5.0, end=5.5)
piano_note_9 = pretty_midi.Note(velocity=100, pitch=80, start=5.5, end=6.0)
piano.notes.extend([piano_note_7, piano_note_8, piano_note_9])

# Sax: motif variation - F (MIDI 65) -> G (MIDI 67) -> A (MIDI 69) -> F (MIDI 65)
sax_note_9 = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875)
sax_note_10 = pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25)
sax_note_11 = pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625)
sax_note_12 = pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0)
sax.notes.extend([sax_note_9, sax_note_10, sax_note_11, sax_note_12])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_21 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_22 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drum_23 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)
drum_24 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
drum_25 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
drum_26 = pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)
drum_27 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
drums.notes.extend([drum_21, drum_22, drum_23, drum_24, drum_25, drum_26, drum_27])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
