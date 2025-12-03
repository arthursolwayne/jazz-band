
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # F2 (chromatic approach)
]

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # C5
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75),  # Eb4
]

# Bar 2: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # B4
]

for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # Eb2 (chromatic approach)
]

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb D F Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # F5
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # Ab4
]

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # B4
]

for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # F2 (chromatic approach)
]

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # C5
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.75),  # Eb4
]

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # B4
]

for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
