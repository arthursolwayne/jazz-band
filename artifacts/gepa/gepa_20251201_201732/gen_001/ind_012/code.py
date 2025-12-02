
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25), # F (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F Ab C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.25),  # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # F (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # D2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 3: Gm7 (G Bb D F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75),  # D4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # F4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: continuation of the motif, bring it back, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25), # F (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # D2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.25),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=5.25),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),  # Bb4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: finish the motif, resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 4
]

# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: repeat for the next bar
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
