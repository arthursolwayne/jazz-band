
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drum_hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_hihat, drum_hihat2, drum_hihat3])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Eb2
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # G2
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # C3
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25), # D3
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # C#3
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # E3
]
bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 - Cm7 - Bbmaj7 - Am7
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Eb5

    # Bar 3: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Bb5

    # Bar 4: Bbmaj7 (Bb, D, F, A)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D6
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F6
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # A6

    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # A6
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C6
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E6
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # G6
]
piano.notes.extend(piano_notes)

# Sax: Dante - one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Fm - start with a motif
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # G4

    # Bar 3: Cm - leave it hanging
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C5

    # Bar 4: Bbmaj7 - come back and finish it
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Bb5
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D6
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # Bb5
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),   # C6
]
sax.notes.extend(sax_notes)

# Drums: Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2, hihat, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
