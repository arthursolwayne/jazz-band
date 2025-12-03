
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # F2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),  # F2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0)   # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # E5
]
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # F5
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=4.5),  # Ab4
])
# Bar 4: D7 (D, F#, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # F#5
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0),  # A5
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # C5 (resolve)
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Bb4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Bb4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # Eb4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
