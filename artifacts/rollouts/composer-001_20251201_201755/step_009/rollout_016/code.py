
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (D3 in MIDI?), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2 (MIDI 50)
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.625), # C2
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
piano_notes = [
    # Bar 2: D7 (D F# A C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C#5

    # Bar 3: Gm7 (G Bb D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # F4

    # Bar 4: Bb7 (Bb D F A)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),  # A4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 4.5]:
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25)

    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4 (62), F#4 (67), A4 (71), D5 (76) — a short melody with a question in the first two notes
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25), # A4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.875), # D4
    pretty_midi.Note(velocity=110, pitch=76, start=2.875, end=3.0)   # D5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
