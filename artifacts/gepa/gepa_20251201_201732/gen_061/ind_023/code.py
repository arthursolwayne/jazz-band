
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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass: Marcus - walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 - D (2) -> C# (1) -> E (3) -> F (4)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.25), # C#2
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # E2
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # F2

    # Bar 3 - F (4) -> E (3) -> G (5) -> A (5)
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # E2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),  # A2

    # Bar 4 - A (5) -> G# (5) -> B (6) -> C (6)
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=80, pitch=44, start=4.875, end=5.25), # G#2
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625), # B2
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),  # C3
]
bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, different chord each bar, resolve on last
# Bar 2: D7sus4 (D, G, C) -> D7 (D, F#, A, C)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
]
# Bar 3: G7sus4 (G, C, D) -> G7 (G, B, D, F)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # F4
]
# Bar 4: C7sus4 (C, F, G) -> C7 (C, E, G, B)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # B4
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax: Dante - one short motif, make it sing
# Motif: D4 (beat 1), E4 (beat 2), D4 (beat 3), C4 (beat 4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),  # C4
    # Repeat the motif with slight variation
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=6.0, end=6.375),  # D4
]
sax.notes.extend(sax_notes)

# Drums in bars 2-4
# Bar 2
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),  # Kick 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare 4
]
# Bar 3
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.3125),  # Kick 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),  # Snare 4
]
# Bar 4
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.8125),  # Kick 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Snare 4
]
# Hi-hats on every eighth in bars 2-4
hi_hat_notes = []
for bar_start in [1.5, 3.0, 4.5]:
    for i in range(8):
        start = bar_start + (i * 0.375)
        end = start + 0.1875
        hi_hat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes_bar2 + drum_notes_bar3 + drum_notes_bar4 + hi_hat_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
