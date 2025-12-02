
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# D Dorian: D, E, F#, G, A, B, C
for bar in range(2, 5):
    start = bar * 1.5
    # Walking bass line
    # Bar 2: D -> Eb -> F -> G
    if bar == 2:
        notes = [pretty_midi.Note(velocity=80, pitch=62, start=start, end=start + 0.375),  # D
                 pretty_midi.Note(velocity=80, pitch=61, start=start + 0.375, end=start + 0.75),  # Eb
                 pretty_midi.Note(velocity=80, pitch=64, start=start + 0.75, end=start + 1.125),  # F
                 pretty_midi.Note(velocity=80, pitch=67, start=start + 1.125, end=start + 1.5)]  # G
    # Bar 3: A -> B -> C -> D
    elif bar == 3:
        notes = [pretty_midi.Note(velocity=80, pitch=69, start=start, end=start + 0.375),  # A
                 pretty_midi.Note(velocity=80, pitch=71, start=start + 0.375, end=start + 0.75),  # B
                 pretty_midi.Note(velocity=80, pitch=72, start=start + 0.75, end=start + 1.125),  # C
                 pretty_midi.Note(velocity=80, pitch=62, start=start + 1.125, end=start + 1.5)]  # D
    # Bar 4: F -> G -> A -> B
    elif bar == 4:
        notes = [pretty_midi.Note(velocity=80, pitch=64, start=start, end=start + 0.375),  # F
                 pretty_midi.Note(velocity=80, pitch=67, start=start + 0.375, end=start + 0.75),  # G
                 pretty_midi.Note(velocity=80, pitch=69, start=start + 0.75, end=start + 1.125),  # A
                 pretty_midi.Note(velocity=80, pitch=71, start=start + 1.125, end=start + 1.5)]  # B
    bass.notes.extend(notes)

# Diane: 7th chords, comp on 2 and 4
# D7: D, F#, A, C
for bar in range(2, 5):
    start = bar * 1.5
    # Bar 2: D7 on 2 and 4
    if bar == 2:
        # 2nd beat
        note1 = pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)
        note2 = pretty_midi.Note(velocity=100, pitch=67, start=start + 0.375, end=start + 0.75)
        note3 = pretty_midi.Note(velocity=100, pitch=71, start=start + 0.375, end=start + 0.75)
        note4 = pretty_midi.Note(velocity=100, pitch=72, start=start + 0.375, end=start + 0.75)
        # 4th beat
        note5 = pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5)
        note6 = pretty_midi.Note(velocity=100, pitch=67, start=start + 1.125, end=start + 1.5)
        note7 = pretty_midi.Note(velocity=100, pitch=71, start=start + 1.125, end=start + 1.5)
        note8 = pretty_midi.Note(velocity=100, pitch=72, start=start + 1.125, end=start + 1.5)
        piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])
    # Bar 3: D7 on 2 and 4
    elif bar == 3:
        # 2nd beat
        note1 = pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)
        note2 = pretty_midi.Note(velocity=100, pitch=67, start=start + 0.375, end=start + 0.75)
        note3 = pretty_midi.Note(velocity=100, pitch=71, start=start + 0.375, end=start + 0.75)
        note4 = pretty_midi.Note(velocity=100, pitch=72, start=start + 0.375, end=start + 0.75)
        # 4th beat
        note5 = pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5)
        note6 = pretty_midi.Note(velocity=100, pitch=67, start=start + 1.125, end=start + 1.5)
        note7 = pretty_midi.Note(velocity=100, pitch=71, start=start + 1.125, end=start + 1.5)
        note8 = pretty_midi.Note(velocity=100, pitch=72, start=start + 1.125, end=start + 1.5)
        piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])
    # Bar 4: D7 on 2 and 4
    elif bar == 4:
        # 2nd beat
        note1 = pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)
        note2 = pretty_midi.Note(velocity=100, pitch=67, start=start + 0.375, end=start + 0.75)
        note3 = pretty_midi.Note(velocity=100, pitch=71, start=start + 0.375, end=start + 0.75)
        note4 = pretty_midi.Note(velocity=100, pitch=72, start=start + 0.375, end=start + 0.75)
        # 4th beat
        note5 = pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5)
        note6 = pretty_midi.Note(velocity=100, pitch=67, start=start + 1.125, end=start + 1.5)
        note7 = pretty_midi.Note(velocity=100, pitch=71, start=start + 1.125, end=start + 1.5)
        note8 = pretty_midi.Note(velocity=100, pitch=72, start=start + 1.125, end=start + 1.5)
        piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs

# Bar 2: Start the motif
start = 1.5
# D, F#, A, G
note1 = pretty_midi.Note(velocity=110, pitch=62, start=start, end=start + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=67, start=start + 0.375, end=start + 0.75)
note3 = pretty_midi.Note(velocity=110, pitch=69, start=start + 0.75, end=start + 1.125)
note4 = pretty_midi.Note(velocity=110, pitch=67, start=start + 1.125, end=start + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Leave it hanging, play G
start = 3.0
note1 = pretty_midi.Note(velocity=110, pitch=67, start=start, end=start + 0.375)
sax.notes.append(note1)

# Bar 4: Come back and finish it
start = 4.5
# F#, A, D
note1 = pretty_midi.Note(velocity=110, pitch=67, start=start, end=start + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=69, start=start + 0.375, end=start + 0.75)
note3 = pretty_midi.Note(velocity=110, pitch=62, start=start + 0.75, end=start + 1.125)
note4 = pretty_midi.Note(velocity=110, pitch=67, start=start + 1.125, end=start + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
