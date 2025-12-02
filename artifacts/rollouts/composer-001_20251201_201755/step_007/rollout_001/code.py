
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.append(kick)
    drums.notes.append(snare)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Diane on piano (Cmaj7 -> Dm7 -> G7 -> Cmaj7)
# Bar 3: Diane on piano (A7 -> Dm7 -> G7 -> Cmaj7)
# Bar 4: Diane on piano (D7 -> G7 -> Cm7 -> F7)

# Bass: Walking line with chromatic approaches
# Bar 2: D2 -> E2 -> F2 -> G2 (D -> E -> F -> G)
# Bar 3: G2 -> A2 -> Bb2 -> B2 (G -> A -> Bb -> B)
# Bar 4: C2 -> Db2 -> D2 -> Eb2 (C -> Db -> D -> Eb)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: D4 - F4 - G4 - Bb4 (D - F - G - Bb)

# Bar 2: sax starts motif
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0)
sax.notes.append(note1)
sax.notes.append(note2)

# Bar 3: leave it hanging
note3 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5)
sax.notes.append(note3)

# Bar 4: finish the motif
note4 = pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0)
sax.notes.append(note4)

# Piano: Bar 2: Cmaj7
note_c = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0)
note_e = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0)
note_g = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0)
note_b = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0)
piano.notes.append(note_c)
piano.notes.append(note_e)
piano.notes.append(note_g)
piano.notes.append(note_b)

# Bar 3: A7
note_a = pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5)
note_c = pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.5)
note_e = pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.5)
note_g = pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5)
note_b = pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5)
note_d = pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5)
piano.notes.append(note_a)
piano.notes.append(note_c)
piano.notes.append(note_e)
piano.notes.append(note_g)
piano.notes.append(note_b)
piano.notes.append(note_d)

# Bar 4: D7
note_d = pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0)
note_f = pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0)
note_a = pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0)
note_c = pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0)
note_e = pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0)
note_g = pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0)
note_b = pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0)
piano.notes.append(note_d)
piano.notes.append(note_f)
piano.notes.append(note_a)
piano.notes.append(note_c)
piano.notes.append(note_e)
piano.notes.append(note_g)
piano.notes.append(note_b)

# Bass: Bar 2: D2 -> E2 -> F2 -> G2
note_d = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75)
note_e = pretty_midi.Note(velocity=100, pitch=39, start=1.75, end=2.0)
note_f = pretty_midi.Note(velocity=100, pitch=40, start=2.0, end=2.25)
note_g = pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.5)
bass.notes.append(note_d)
bass.notes.append(note_e)
bass.notes.append(note_f)
bass.notes.append(note_g)

# Bar 3: G2 -> A2 -> Bb2 -> B2
note_g = pretty_midi.Note(velocity=100, pitch=41, start=2.5, end=2.75)
note_a = pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=3.0)
note_bb = pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.25)
note_b = pretty_midi.Note(velocity=100, pitch=44, start=3.25, end=3.5)
bass.notes.append(note_g)
bass.notes.append(note_a)
bass.notes.append(note_bb)
bass.notes.append(note_b)

# Bar 4: C2 -> Db2 -> D2 -> Eb2
note_c = pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.75)
note_db = pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=4.0)
note_d = pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.25)
note_eb = pretty_midi.Note(velocity=100, pitch=39, start=4.25, end=4.5)
bass.notes.append(note_c)
bass.notes.append(note_db)
bass.notes.append(note_d)
bass.notes.append(note_eb)

# Drums: Bar 2
for bar in range(1):
    start = 1.5 + bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.append(kick)
    drums.notes.append(snare)

# Drums: Bar 3
start = 3.0
kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    drums.notes.append(hihat)
drums.notes.append(kick)
drums.notes.append(snare)

# Drums: Bar 4
start = 4.5
kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    drums.notes.append(hihat)
drums.notes.append(kick)
drums.notes.append(snare)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
