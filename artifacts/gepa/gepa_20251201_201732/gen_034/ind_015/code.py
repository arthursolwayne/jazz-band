
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),  # Eb2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # D2
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),  # G2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: C7 (F, Bb, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # E5
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.875),  # G5
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=1.875),  # Bb5
    # Bar 3: G7 (B, D, F, G)
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=83, start=3.0, end=3.375),  # F5
    # Bar 4: Bb7 (D, F, A, Bb)
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=90, pitch=83, start=4.5, end=4.875),  # F5
    pretty_midi.Note(velocity=90, pitch=86, start=4.5, end=4.875),  # A5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Motif: F (65), Ab (67), Bb (69), F (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),   # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.625, end=3.75), # F4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),   # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=5.125, end=5.25), # F4
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
