
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Bb, Eb, Ab), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625), # Eb2
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),  # Bb2
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # Db2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125), # Eb2
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),  # Bb2
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=54, start=4.875, end=5.25), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625), # Eb2
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chords each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # C5
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875), # D5
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # F5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # Ab4
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # Eb4
]
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Melody starts
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875), # Eb4
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25), # G4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # F#4
    # Bar 3: Continue the motif, leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375), # Eb4
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75), # G4
    # Bar 4: Bring it back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875), # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25), # G4
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625), # Eb4
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # F#4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
