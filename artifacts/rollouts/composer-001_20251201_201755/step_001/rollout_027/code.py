
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_note_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_note_2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_note_3 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_note_4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_note_1, drum_note_2, drum_note_3, drum_note_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_note_1 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)  # D2
bass_note_2 = pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25)  # F#2
bass_note_3 = pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625)  # A2
bass_note_4 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)  # D2

bass_note_5 = pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375)  # A2
bass_note_6 = pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75)  # F#2
bass_note_7 = pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125)  # G#2
bass_note_8 = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)  # D2

bass_note_9 = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)  # D2
bass_note_10 = pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25)  # F#2
bass_note_11 = pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625)  # A2
bass_note_12 = pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)  # D2

bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4,
                   bass_note_5, bass_note_6, bass_note_7, bass_note_8,
                   bass_note_9, bass_note_10, bass_note_11, bass_note_12])

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D major 7 (D, F#, A, C#)
piano_note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
piano_note_2 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875)
piano_note_3 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875)
piano_note_4 = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875)

# Bar 3: F# minor 7 (F#, A, C#, E)
piano_note_5 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375)
piano_note_6 = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375)
piano_note_7 = pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375)
piano_note_8 = pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375)

# Bar 4: B7 (B, D#, F#, A)
piano_note_9 = pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875)
piano_note_10 = pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875)
piano_note_11 = pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875)
piano_note_12 = pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875)

piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4,
                    piano_note_5, piano_note_6, piano_note_7, piano_note_8,
                    piano_note_9, piano_note_10, piano_note_11, piano_note_12])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_note_5 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_note_6 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_note_7 = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
drum_note_8 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)
drum_note_9 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)
drum_note_10 = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
drum_note_11 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
drum_note_12 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)

# Bar 3 (3.0 - 4.5s)
drum_note_13 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_note_14 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drum_note_15 = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)
drum_note_16 = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)
drum_note_17 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)
drum_note_18 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
drum_note_19 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
drum_note_20 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)

# Bar 4 (4.5 - 6.0s)
drum_note_21 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_note_22 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drum_note_23 = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)
drum_note_24 = pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)
drum_note_25 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)
drum_note_26 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
drum_note_27 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
drum_note_28 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)

drums.notes.extend([drum_note_5, drum_note_6, drum_note_7, drum_note_8,
                    drum_note_9, drum_note_10, drum_note_11, drum_note_12,
                    drum_note_13, drum_note_14, drum_note_15, drum_note_16,
                    drum_note_17, drum_note_18, drum_note_19, drum_note_20,
                    drum_note_21, drum_note_22, drum_note_23, drum_note_24,
                    drum_note_25, drum_note_26, drum_note_27, drum_note_28])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (67), A (71), D (62) - but fragmented, left hanging, then completed

# First note in bar 2 (start at 1.5)
sax_note_1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875)

# Second note in bar 2 (start at 1.875)
sax_note_2 = pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25)

# Third note in bar 3 (start at 3.0)
sax_note_3 = pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375)

# Fourth note in bar 4 (start at 4.5)
sax_note_4 = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875)

# Long note in bar 4 (start at 5.25)
sax_note_5 = pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=6.0)

sax.notes.extend([sax_note_1, sax_note_2, sax_note_3, sax_note_4, sax_note_5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
