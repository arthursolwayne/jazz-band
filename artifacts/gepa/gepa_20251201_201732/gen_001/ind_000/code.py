
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
drum_note_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)  # Kick on 1
drum_note_2 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125) # Snare on 2
drum_note_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)  # Kick on 3
drum_note_4 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)    # Hihat on every eighth
drums.notes.extend([drum_note_1, drum_note_2, drum_note_3, drum_note_4])

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: walking line, roots and fifths with chromatic approaches
bass_note_1 = pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875)  # D2 (root) with chromatic approach
bass_note_2 = pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25) # D#2 (chromatic)
bass_note_3 = pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625) # A2 (fifth)
bass_note_4 = pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0)  # G2 (chromatic)
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4])

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)  # D4
piano_note_2 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875)  # F#4
piano_note_3 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875)  # A4
piano_note_4 = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875)  # C#4
piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_note_5 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)  # Kick on 1
drum_note_6 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25) # Snare on 2
drum_note_7 = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625) # Kick on 3
drum_note_8 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)  # Snare on 4
drum_note_9 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)    # Hihat on every eighth
drums.notes.extend([drum_note_5, drum_note_6, drum_note_7, drum_note_8, drum_note_9])

# Dante: Tenor sax - motif, start it, leave it hanging, come back and finish it
# Motif: D4, F4, G4, D4 (play first two notes)
sax_note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)  # D4
sax_note_2 = pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25) # F4
sax.notes.extend([sax_note_1, sax_note_2])

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: walking line, roots and fifths with chromatic approaches
bass_note_5 = pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375)  # G2 (chromatic)
bass_note_6 = pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75) # A2 (fifth)
bass_note_7 = pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125) # D2 (root)
bass_note_8 = pretty_midi.Note(velocity=100, pitch=51, start=4.125, end=4.5)  # D#2 (chromatic)
bass.notes.extend([bass_note_5, bass_note_6, bass_note_7, bass_note_8])

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G, B, D, F#)
piano_note_5 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375)  # G4
piano_note_6 = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375)  # B4
piano_note_7 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375)  # D4
piano_note_8 = pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375)  # F#4
piano.notes.extend([piano_note_5, piano_note_6, piano_note_7, piano_note_8])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_note_10 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)  # Kick on 1
drum_note_11 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75) # Snare on 2
drum_note_12 = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125) # Kick on 3
drum_note_13 = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)  # Snare on 4
drum_note_14 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)    # Hihat on every eighth
drums.notes.extend([drum_note_10, drum_note_11, drum_note_12, drum_note_13, drum_note_14])

# Dante: Tenor sax - motif continuation, finish it
# Motif: G4, D4
sax_note_3 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375)  # G4
sax_note_4 = pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75) # D4
sax.notes.extend([sax_note_3, sax_note_4])

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: walking line, roots and fifths with chromatic approaches
bass_note_9 = pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875)  # D#2 (chromatic)
bass_note_10 = pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25) # D2 (root)
bass_note_11 = pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625) # A2 (fifth)
bass_note_12 = pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0)  # G2 (chromatic)
bass.notes.extend([bass_note_9, bass_note_10, bass_note_11, bass_note_12])

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cmaj7 (C, E, G, B)
piano_note_9 = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875)  # C4
piano_note_10 = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875) # E4
piano_note_11 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875) # G4
piano_note_12 = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875) # B4
piano.notes.extend([piano_note_9, piano_note_10, piano_note_11, piano_note_12])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_note_15 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)  # Kick on 1
drum_note_16 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25) # Snare on 2
drum_note_17 = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625) # Kick on 3
drum_note_18 = pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)  # Snare on 4
drum_note_19 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)    # Hihat on every eighth
drums.notes.extend([drum_note_15, drum_note_16, drum_note_17, drum_note_18, drum_note_19])

# Dante: Tenor sax - motif end, resolve it
# Motif: C4 (resolve)
sax_note_5 = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875)  # C4
sax.notes.append(sax_note_5)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
