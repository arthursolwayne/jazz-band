
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

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Fm7 (F, Ab, D, C)
bass_note_1 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)  # F
bass_note_2 = pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25)  # Ab
bass_note_3 = pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625)  # G
bass_note_4 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)  # F
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4])

# Bar 3: Bb7 (Bb, D, F, Ab)
bass_note_5 = pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375)  # Bb
bass_note_6 = pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75)  # D
bass_note_7 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)  # C
bass_note_8 = pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5)  # Bb
bass.notes.extend([bass_note_5, bass_note_6, bass_note_7, bass_note_8])

# Bar 4: Cm7 (C, Eb, G, Bb)
bass_note_9 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)  # C
bass_note_10 = pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25)  # Eb
bass_note_11 = pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625)  # D
bass_note_12 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)  # C
bass.notes.extend([bass_note_9, bass_note_10, bass_note_11, bass_note_12])

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: Fm7
piano_note_1 = pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.25)  # F
piano_note_2 = pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=2.25)  # Ab
piano_note_3 = pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=2.25)  # D
piano_note_4 = pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=2.25)  # C
piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4])

# Bar 3: Bb7
piano_note_5 = pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.75)  # Bb
piano_note_6 = pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.75)  # D
piano_note_7 = pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.75)  # F
piano_note_8 = pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.75)  # Ab
piano.notes.extend([piano_note_5, piano_note_6, piano_note_7, piano_note_8])

# Bar 4: Cm7
piano_note_9 = pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=5.25)  # C
piano_note_10 = pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=5.25)  # Eb
piano_note_11 = pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=5.25)  # D
piano_note_12 = pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=5.25)  # Bb
piano.notes.extend([piano_note_9, piano_note_10, piano_note_11, piano_note_12])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_note_5 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)  # Kick
drum_note_6 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)  # Snare
drum_note_7 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)  # Hihat
drum_note_8 = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)  # Hihat
drum_note_9 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)  # Hihat
drum_note_10 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)  # Hihat
drums.notes.extend([drum_note_5, drum_note_6, drum_note_7, drum_note_8, drum_note_9, drum_note_10])

# Bar 3
drum_note_11 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)  # Kick
drum_note_12 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)  # Snare
drum_note_13 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)  # Hihat
drum_note_14 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)  # Hihat
drum_note_15 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)  # Hihat
drum_note_16 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)  # Hihat
drums.notes.extend([drum_note_11, drum_note_12, drum_note_13, drum_note_14, drum_note_15, drum_note_16])

# Bar 4
drum_note_17 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)  # Kick
drum_note_18 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)  # Snare
drum_note_19 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)  # Hihat
drum_note_20 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)  # Hihat
drum_note_21 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)  # Hihat
drum_note_22 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)  # Hihat
drums.notes.extend([drum_note_17, drum_note_18, drum_note_19, drum_note_20, drum_note_21, drum_note_22])

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Bar 2: Tenor sax motif
sax_note_1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)  # Gm
sax_note_2 = pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0)  # A
sax_note_3 = pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25)  # Gm
sax_note_4 = pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5)  # F
sax.notes.extend([sax_note_1, sax_note_2, sax_note_3, sax_note_4])

# Bar 3: Continue the motif
sax_note_5 = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25)  # Gm
sax_note_6 = pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5)  # A
sax_note_7 = pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75)  # Gm
sax_note_8 = pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0)  # F
sax.notes.extend([sax_note_5, sax_note_6, sax_note_7, sax_note_8])

# Bar 4: End the motif
sax_note_9 = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75)  # Gm
sax_note_10 = pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0)  # A
sax_note_11 = pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25)  # Gm
sax_note_12 = pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5)  # F
sax.notes.extend([sax_note_9, sax_note_10, sax_note_11, sax_note_12])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
