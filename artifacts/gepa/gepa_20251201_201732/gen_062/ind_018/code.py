
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Walking line, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2: Fm7 (F, C, Ab, D)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=58, start=1.875, end=2.25), # C3
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # D3
    # Bar 3: Bb7 (Bb, F, D, A)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125), # D3
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # A3
    # Bar 4: Eb7 (Eb, Bb, G, D)
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # Bb2
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625), # G3
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Ab2
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # C3
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # D3
    # Bar 3: Bb7 (Bb, D, F, A)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # D3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # A3
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # G3
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # D3
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - Eb - C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # Bb2
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625),  # Eb2
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),   # C2
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2 (repeat)
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # Bb2 (repeat)
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),  # C2 (resolve)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # D3 (return)
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),  # F2 (complete)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
# Hihat on every eighth
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    for t in [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]:
        pretty_midi.Note(velocity=100, pitch=42, start=start + t, end=start + t + 0.375)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
# midi.write disabled
