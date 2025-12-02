
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS LINE (Marcus): Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),   # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625),  # Ab (fifth)
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),   # G (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),   # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),  # D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),  # Ab (fifth)
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),   # G (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),   # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625),  # Ab (fifth)
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0),   # G (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# PIANO (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F Ab C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Eb
]
# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Ab
])
# Bar 4: Eb7 (Eb G Bb D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D
])
# Resolve to Am7 (A C E G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # G
])
for note in piano_notes:
    piano.notes.append(note)

# SAX (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - Bb - F (melodic gesture)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.6875, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.5625, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.9375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.9375, end=4.125),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Bar 1 (start=1.5)
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875),  # Hihat on 4
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
midi.write("jazz_piece.mid")
