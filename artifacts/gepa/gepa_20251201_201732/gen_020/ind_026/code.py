
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
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
              pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)]
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
               pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)]
hihat_notes = []
for i in range(4):
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i * 0.375, end=i * 0.375 + 0.1875))

drums.notes.extend(kick_notes)
drums.notes.extend(snare_notes)
drums.notes.extend(hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, roots and fifths with chromatic approaches
# Fm7: F, C, Ab, D
# Bar 2: F, Eb, C, Bb (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=34, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=37, start=2.625, end=3.0),  # Bb

    # Bar 3: Ab, G, D, C (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),  # C

    # Bar 4: F, Eb, Ab, G (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=34, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=39, start=5.625, end=6.0)   # G
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=34, start=1.5, end=2.0),  # Eb

    # Bar 3: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=40, start=2.0, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=34, start=2.0, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=39, start=2.0, end=2.5),  # G

    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Bb, C, F (octave up)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=33, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75),  # F (octave up)
]
sax.notes.extend(sax_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for i in range(4):
        hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=(bar * 1.5) + i * 0.375, end=(bar * 1.5) + i * 0.375 + 0.1875))
    kick_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=(bar * 1.5), end=(bar * 1.5) + 0.375))
    kick_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=(bar * 1.5) + 1.125, end=(bar * 1.5) + 1.5))
    snare_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=(bar * 1.5) + 0.375, end=(bar * 1.5) + 0.75))
    snare_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=(bar * 1.5) + 1.5, end=(bar * 1.5) + 1.875))

drums.notes.extend(hihat_notes)
drums.notes.extend(kick_notes)
drums.notes.extend(snare_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
