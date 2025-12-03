
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 to C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (F7 chord) - F, C, B, F
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # C4
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # F3
    # Bar 3 (B7 chord) - B, F#, E, B
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # B3
    pretty_midi.Note(velocity=100, pitch=81, start=3.375, end=3.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=80, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),  # B3
    # Bar 4 (E7 chord) - E, B, A, E
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # E3
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),  # B3
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),  # A3
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # E3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
piano_notes = [
    # Bar 2 - F7 chord (F, A, C, E, B)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # E5
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875),  # B5
    # Bar 3 - B7 chord (B, D#, F#, A#, D)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=3.375),  # D#5
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # F#5
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.375),  # A#5
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),  # D5
    # Bar 4 - E7 chord (E, G#, B, D#, G)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # G#4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # D#5
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),  # G4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # E4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # E4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # E4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
