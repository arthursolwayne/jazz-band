
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Bar 1: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75), # snare on 2
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125), # kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),  # snare on 4
    # hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) to F2 (41) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25), # chromatic
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625), # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # G2

    # Bar 3: Bb2 (40) to C2 (36) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.75), # chromatic
    pretty_midi.Note(velocity=80, pitch=36, start=3.75, end=4.125), # C2
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # D2

    # Bar 4: F2 (41) to A2 (45) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # chromatic
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Piano: Diane, open voicings, different chord each bar, resolve on last
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C#4

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # Ab4

    # Bar 4: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # E5
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4 (1.5 - 6.0s)
for bar_start in [1.5, 3.0, 4.5]:
    # kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    drum_notes = [
        pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375),  # kick on 1
        pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75), # snare on 2
        pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125), # kick on 3
        pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5),  # snare on 4
        # hihat on every eighth
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.0, end=bar_start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    ]
    drums.notes.extend(drum_notes)

# Sax: Dante, one short motif, start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif on 2 (0.375 into bar)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 0.375, end=1.5 + 0.75),  # D4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5 + 0.75, end=1.5 + 1.125),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 1.125, end=1.5 + 1.5),   # G4

    # Bar 3: No notes — let it hang

    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=100, pitch=65, start=4.5 + 0.375, end=4.5 + 0.75),  # D4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5 + 0.75, end=4.5 + 1.125),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5 + 1.125, end=4.5 + 1.5),   # G4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
