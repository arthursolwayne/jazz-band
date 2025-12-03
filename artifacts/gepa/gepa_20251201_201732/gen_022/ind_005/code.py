
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

# Kick on 1 and 3
drum_note_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_note_2 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_note_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drum_note_4 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_note_1, drum_note_2, drum_note_3, drum_note_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_note_1 = pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.875)
bass_note_2 = pretty_midi.Note(velocity=110, pitch=40, start=1.875, end=2.25)
bass_note_3 = pretty_midi.Note(velocity=110, pitch=43, start=2.25, end=2.625)
bass_note_4 = pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=3.0)
bass_note_5 = pretty_midi.Note(velocity=110, pitch=40, start=3.0, end=3.375)
bass_note_6 = pretty_midi.Note(velocity=110, pitch=43, start=3.375, end=3.75)
bass_note_7 = pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125)
bass_note_8 = pretty_midi.Note(velocity=110, pitch=40, start=4.125, end=4.5)
bass_note_9 = pretty_midi.Note(velocity=110, pitch=43, start=4.5, end=4.875)
bass_note_10 = pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25)
bass_note_11 = pretty_midi.Note(velocity=110, pitch=40, start=5.25, end=5.625)
bass_note_12 = pretty_midi.Note(velocity=110, pitch=43, start=5.625, end=6.0)
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4, bass_note_5, bass_note_6, bass_note_7, bass_note_8, bass_note_9, bass_note_10, bass_note_11, bass_note_12])

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
piano_note_2 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875)
piano_note_3 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875)
piano_note_4 = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875)
piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4])

# Bar 3: G7 (G B D F)
piano_note_5 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)
piano_note_6 = pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625)
piano_note_7 = pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625)
piano_note_8 = pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625)
piano.notes.extend([piano_note_5, piano_note_6, piano_note_7, piano_note_8])

# Bar 4: Cm7 (C Eb G Bb)
piano_note_9 = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375)
piano_note_10 = pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375)
piano_note_11 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375)
piano_note_12 = pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375)
piano.notes.extend([piano_note_9, piano_note_10, piano_note_11, piano_note_12])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_note_5 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_note_6 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_note_7 = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
drum_note_8 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25)
drums.notes.extend([drum_note_5, drum_note_6, drum_note_7, drum_note_8])

# Bar 3
drum_note_9 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875)
drum_note_10 = pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)
drum_note_11 = pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.625)
drum_note_12 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.375)
drums.notes.extend([drum_note_9, drum_note_10, drum_note_11, drum_note_12])

# Bar 4
drum_note_13 = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)
drum_note_14 = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)
drum_note_15 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_note_16 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5)
drums.notes.extend([drum_note_13, drum_note_14, drum_note_15, drum_note_16])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - A - (rest) - D - F - A
sax_note_1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)
sax_note_2 = pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0)
sax_note_3 = pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25)
sax_note_4 = pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.875)
sax_note_5 = pretty_midi.Note(velocity=110, pitch=65, start=2.875, end=3.125)
sax_note_6 = pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.375)
sax.notes.extend([sax_note_1, sax_note_2, sax_note_3, sax_note_4, sax_note_5, sax_note_6])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
