
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

# Bass line (Marcus)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.0625), # Gb
    pretty_midi.Note(velocity=100, pitch=46, start=2.0625, end=2.25), # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.4375), # Gb
    pretty_midi.Note(velocity=100, pitch=44, start=2.4375, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=2.8125), # Ab
    pretty_midi.Note(velocity=100, pitch=44, start=2.8125, end=3.0), # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.1875), # Ab
    pretty_midi.Note(velocity=100, pitch=46, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.5625), # Gb
    pretty_midi.Note(velocity=100, pitch=44, start=3.5625, end=3.75), # F
    # Bar 4 continuation
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=3.9375), # G
    pretty_midi.Note(velocity=100, pitch=45, start=3.9375, end=4.125), # Gb
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.3125, end=4.5), # G
    # Bar 4 final
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.6875), # Gb
    pretty_midi.Note(velocity=100, pitch=44, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.0625), # Ab
    pretty_midi.Note(velocity=100, pitch=44, start=5.0625, end=5.25), # F
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.75), # C7
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75), # C#7
    pretty_midi.Note(velocity=100, pitch=57, start=2.0, end=2.25), # A6
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.25), # A#6
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75), # D7
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=2.75), # D#7
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.25), # C7
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25), # C#7
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75), # E7
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75), # F7
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25), # D7
    pretty_midi.Note(velocity=100, pitch=63, start=4.0, end=4.25), # D#7
    # Bar 4 continuation
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.75), # C7
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75), # C#7
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25), # E7
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25), # F7
]
piano.notes.extend(piano_notes)

# Sax (Dante)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # D7
    pretty_midi.Note(velocity=110, pitch=63, start=1.6875, end=1.875), # D#7
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0625), # E7
    pretty_midi.Note(velocity=110, pitch=65, start=2.0625, end=2.25), # F7
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375), # D7
    pretty_midi.Note(velocity=110, pitch=63, start=2.4375, end=2.625), # D#7
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.8125), # E7
    pretty_midi.Note(velocity=110, pitch=65, start=2.8125, end=3.0), # F7
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875), # D7
    pretty_midi.Note(velocity=110, pitch=63, start=3.1875, end=3.375), # D#7
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5625), # E7
    pretty_midi.Note(velocity=110, pitch=65, start=3.5625, end=3.75), # F7
    # Bar 4 continuation
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.9375), # D7
    pretty_midi.Note(velocity=110, pitch=63, start=3.9375, end=4.125), # D#7
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.3125), # E7
    pretty_midi.Note(velocity=110, pitch=65, start=4.3125, end=4.5), # F7
    # Bar 4 final
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875), # D7
    pretty_midi.Note(velocity=110, pitch=63, start=4.6875, end=4.875), # D#7
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0625), # E7
    pretty_midi.Note(velocity=110, pitch=65, start=5.0625, end=5.25), # F7
]
sax.notes.extend(sax_notes)

# Drums in bars 2-4
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
