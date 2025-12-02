
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick, snare, hihat])

# Bar 2: All instruments in
# Sax: Melody starts here, a simple motif
# Dm7 -> G7 -> Cm7 -> F7
# Motif: D (D4) -> F (F4) -> C (C4) -> D (D4) -> (leave hanging)

note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
# Bar 2: D (D2) -> Eb (Eb2) -> F (F2) -> G (G2)
note1 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=100, pitch=39, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=100, pitch=41, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.5)
bass.notes.extend([note1, note2, note3, note4])

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0)
note2 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0)
note4 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0)
piano.notes.extend([note1, note2, note3, note4])

# Bar 3: G7 (G, B, D, F)
note1 = pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0)
note2 = pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0)
note4 = pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0)
piano.notes.extend([note1, note2, note3, note4])

# Bar 4: Cm7 (C, Eb, G, Bb)
note1 = pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0)
note2 = pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=4.0)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0)
note4 = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0)
piano.notes.extend([note1, note2, note3, note4])

# Bar 3: Sax continues motif
note1 = pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75)
note2 = pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0)
note3 = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25)
note4 = pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)
sax.notes.extend([note1, note2, note3, note4])

# Bar 4: Sax completes motif
note1 = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75)
note2 = pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0)
note3 = pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25)
note4 = pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5)
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Bass continues walking line
# G (G2) -> A (A2) -> Bb (Bb2) -> C (C3)
note1 = pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.75)
note2 = pretty_midi.Note(velocity=100, pitch=45, start=2.75, end=3.0)
note3 = pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.25)
note4 = pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.5)
bass.notes.extend([note1, note2, note3, note4])

# Bar 4: Bass continues walking line
# C (C3) -> Db (Db3) -> D (D3) -> Eb (Eb3)
note1 = pretty_midi.Note(velocity=100, pitch=48, start=3.5, end=3.75)
note2 = pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.0)
note3 = pretty_midi.Note(velocity=100, pitch=50, start=4.0, end=4.25)
note4 = pretty_midi.Note(velocity=100, pitch=51, start=4.25, end=4.5)
bass.notes.extend([note1, note2, note3, note4])

# Bar 3 and 4: Drums continue
# Bar 3
kick = pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=4.0)
drums.notes.extend([kick, snare, hihat])

# Bar 4
kick = pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.375)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.5)
drums.notes.extend([kick, snare, hihat])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
