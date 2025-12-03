
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Ab (E2)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # C (G2)
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # Bb (F2)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif 1 (F, G, Bb, A)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=68, start=2.0625, end=2.25),
    # Bar 3: Motif 2 (G, F, A, G)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=110, pitch=65, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=110, pitch=68, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=110, pitch=67, start=2.8125, end=3.0),
    # Bar 4: Motif 3 (F, G, A, F)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=65, start=3.5625, end=3.75),
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Drums continue with same pattern
# Bar 3: Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
for i in range(3):
    start = 3.0 + i * 1.5
    kick_start = start + 0.0
    kick_end = start + 0.375
    snare_start = start + 0.75
    snare_end = start + 0.875
    hihat_start = start + 0.0
    hihat_end = start + 0.1875
    hihat_start2 = start + 0.1875
    hihat_end2 = start + 0.375
    hihat_start3 = start + 0.375
    hihat_end3 = start + 0.5625
    hihat_start4 = start + 0.5625
    hihat_end4 = start + 0.75
    hihat_start5 = start + 0.75
    hihat_end5 = start + 0.9375
    hihat_start6 = start + 0.9375
    hihat_end6 = start + 1.125
    hihat_start7 = start + 1.125
    hihat_end7 = start + 1.3125
    hihat_start8 = start + 1.3125
    hihat_end8 = start + 1.5

    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end),
        pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end),
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end),
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start2, end=hihat_end2),
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start3, end=hihat_end3),
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start4, end=hihat_end4),
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start5, end=hihat_end5),
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start6, end=hihat_end6),
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start7, end=hihat_end7),
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start8, end=hihat_end8),
    ]
    drums.notes.extend(drum_notes)

# Bar 4: Add kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Already added above

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
