
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_note_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_note_2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_note_3 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_note_4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_note_1, drum_note_2, drum_note_3, drum_note_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_note_1 = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875)  # D2
bass_note_2 = pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25) # Eb2 (chromatic approach)
bass_note_3 = pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625) # G2
bass_note_4 = pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0)  # A2 (chromatic approach)
bass_note_5 = pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375)  # D2
bass_note_6 = pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75) # Eb2
bass_note_7 = pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125) # G2
bass_note_8 = pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5)  # Ab2 (chromatic approach)
bass_note_9 = pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875)  # D2
bass_note_10 = pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25) # Eb2
bass_note_11 = pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625) # G2
bass_note_12 = pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0)  # A2
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4, bass_note_5, bass_note_6, bass_note_7, bass_note_8, bass_note_9, bass_note_10, bass_note_11, bass_note_12])

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_note_1 = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875) # D4
piano_note_2 = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875) # F#4
piano_note_3 = pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875) # A4
piano_note_4 = pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875) # C4
# Bar 3: G7 (G B D F)
piano_note_5 = pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625) # G4
piano_note_6 = pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625) # B4
piano_note_7 = pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625) # D4
piano_note_8 = pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625) # F4
# Bar 4: A7 (A C# E G)
piano_note_9 = pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375) # A4
piano_note_10 = pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375) # C#4
piano_note_11 = pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375) # E4
piano_note_12 = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375) # G4
piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4, piano_note_5, piano_note_6, piano_note_7, piano_note_8, piano_note_9, piano_note_10, piano_note_11, piano_note_12])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_note_5 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_note_6 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_note_7 = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
drum_note_8 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)
drum_note_9 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0)
drum_note_10 = pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.5)
drum_note_11 = pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=3.0)
# Bar 3
drum_note_12 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_note_13 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drum_note_14 = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)
drum_note_15 = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)
drum_note_16 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5)
drum_note_17 = pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=4.0)
drum_note_18 = pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.5)
# Bar 4
drum_note_19 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_note_20 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drum_note_21 = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)
drum_note_22 = pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)
drum_note_23 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0)
drum_note_24 = pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.5)
drum_note_25 = pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=6.0)
drums.notes.extend([drum_note_5, drum_note_6, drum_note_7, drum_note_8, drum_note_9, drum_note_10, drum_note_11, drum_note_12, drum_note_13, drum_note_14, drum_note_15, drum_note_16, drum_note_17, drum_note_18, drum_note_19, drum_note_20, drum_note_21, drum_note_22, drum_note_23, drum_note_24, drum_note_25])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4, F#4, D4 (start on 1.5s, end on 1.875s)
sax_note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
# G4, A4 (start on 2.25s, end on 2.625s)
sax_note_2 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)
sax_note_3 = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625)
# D4, F#4 (start on 3.0s, end on 3.375s)
sax_note_4 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375)
sax_note_5 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375)
# D4 (start on 4.5s, end on 4.875s)
sax_note_6 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)
sax.notes.extend([sax_note_1, sax_note_2, sax_note_3, sax_note_4, sax_note_5, sax_note_6])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_moment.mid")
