
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
# Dm7: D F A C
bass_notes = [
    # Bar 2: Dm7 walking
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D

    # Bar 3: Dm7 walking
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D

    # Bar 4: Dm7 walking
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D F A C
# Bar 2: comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # C

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # C

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 scale: D Eb F G A Bb C D
# Motif: D -> Eb -> F -> D (leaving it hanging on F)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625), # F

    # Bar 3
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125), # Bb

    # Bar 4
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Bars 2-4: Drums continue
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
