
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet
# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bass: Marcus (Walking line in D, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # B2 (chromatic approach)

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # B2
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=100, pitch=51, start=4.125, end=4.5),  # Eb2

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # D2
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),  # B2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (Open voicings, different chord each bar, resolve on last)
# Bar 2: Dmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # C5
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # E5

    # Bar 3: Bm7
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # E5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # F#5
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375), # A5

    # Bar 4: G7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # D5
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875), # F5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (One short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G4

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # B4

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C5
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # B4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
