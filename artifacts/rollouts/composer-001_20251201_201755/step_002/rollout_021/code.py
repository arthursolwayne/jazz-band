
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
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: F (G4) -> A (A4) -> G (G4) -> F (F4), 16th notes
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875), # F (G4)
    pretty_midi.Note(velocity=110, pitch=73, start=1.875, end=2.25), # A (A4)
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625), # G (G4)
    pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=3.0)  # F (F4)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approach on first note
# F -> Gb (approach) -> G -> A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875), # F (F2)
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25), # Gb (Gb2)
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # G (G2)
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0)  # A (A2)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F (F2)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A (A2)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # C (C2)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875)  # E (E2)
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif repeated with a half-step up (F#)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375), # F# (F#4)
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75), # Bb (Bb4)
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125), # F# (F#4)
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5)  # F (F4)
]
sax.notes.extend(sax_notes)

# Bass: Walking line, G -> Ab (approach) -> A -> Bb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375), # G (G2)
    pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.75), # Ab (Ab2)
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # A (A2)
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5)  # Bb (Bb2)
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G (G2)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # Bb (Bb2)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # D (D2)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375)  # F (F2)
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif ends on F (full resolution)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875), # F (F4)
    pretty_midi.Note(velocity=110, pitch=73, start=4.875, end=5.25), # A (A4)
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625), # G (G4)
    pretty_midi.Note(velocity=110, pitch=70, start=5.625, end=6.0)  # F (F4)
]
sax.notes.extend(sax_notes)

# Bass: Walking line, A -> Bb (approach) -> Bb -> C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875), # A (A2)
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25), # Bb (Bb2)
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625), # Bb (Bb2)
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0)  # C (C2)
]
bass.notes.extend(bass_notes)

# Piano: C7 (C, E, G, B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # C (C2)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # E (E2)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G (G2)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875)  # B (B2)
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
for bar in [3, 4]:
    start = bar * 1.5
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75), # Snare on 2
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125), # Kick on 3
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),  # Snare on 4
        # Hi-hats on every eighth
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
