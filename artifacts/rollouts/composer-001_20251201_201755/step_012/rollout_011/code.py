
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # F2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=3.0),  # D4 (root)
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=3.0),  # G4 (fifth)
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=3.0),  # A4 (minor 7)
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=3.0),  # F4 (minor 3)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3 (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),   # Eb2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: G7
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=4.5),  # G4 (root)
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=4.5),  # C5 (major 7)
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=4.5),  # B4 (dominant 7)
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=4.5),  # D5 (major 3)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4 (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),   # G2 (fifth)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: Cm7
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=6.0),  # C4 (root)
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=6.0),  # F4 (minor 7)
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=6.0),  # G4 (minor 3)
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=6.0),  # E4 (fifth)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
