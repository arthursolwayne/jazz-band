
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=54, start=1.875, end=2.25), # F#2
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # A2 (Fm7 root)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75), # A#2
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.125), # B2
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # C3 (Fm7 root)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25), # C#3
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D3
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # E3 (Fm7 root)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, D, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F2
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=3.0),  # Ab2
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # D3
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C3

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # Bb2
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # D3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F2
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=4.5),  # Ab2

    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),  # Eb2
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # G2
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # Bb2
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=6.0),  # Db2
]
for note in piano_notes:
    piano.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, C in 8th notes, then a rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),  # Bb2
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # C3
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2 (reprise)
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625),  # Bb2
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # C3
]
for note in sax_notes:
    sax.notes.append(note)

# Add hihat on every eighth in bars 2-4
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    for eighth in [0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]:
        pretty_midi.Note(velocity=100, pitch=42, start=start + eighth, end=start + eighth + 0.375)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
