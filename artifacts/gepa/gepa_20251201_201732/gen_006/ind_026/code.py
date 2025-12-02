
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
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),  # D3 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # A (E4)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # C (F4)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # E (A4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G4 (motif start)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # B4 (motif continuation)
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625), # G4 (motif continuation)
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # F4 (motif resolution)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.375),  # D3 (root)
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75), # F#3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125), # G3 (fifth)
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),  # A3 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbmaj7 (Bb D F A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),  # Bb (D4)
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=4.5),  # D (G4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # F (Bb4)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),  # A (D5)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B4 (motif continuation)
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # G4 (motif continuation)
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F4 (motif continuation)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # E4 (motif resolution)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # A3 (root)
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25), # C4 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625), # D4 (fifth)
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # Eb4 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),  # D (F4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # F (A4)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # A (D5)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C (F5)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif, end on the final note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # E4 (motif continuation)
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F4 (motif continuation)
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # G4 (motif continuation)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # B4 (motif resolution)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
