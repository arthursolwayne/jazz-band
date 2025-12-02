
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
# Walking line in Dm: D, F, G, A, D, F, G, A, etc.
# Chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane)
# 7th chords on 2 and 4, comping
# Dm7 = D, F, A, C
# G7 = G, B, D, F
# Bm7 = B, D, F#, A
# F7 = F, A, C, E
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.875), # C
    # Bar 3: G7
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=2.875), # G
    pretty_midi.Note(velocity=95, pitch=71, start=2.625, end=2.875), # B
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=2.875), # D
    pretty_midi.Note(velocity=95, pitch=64, start=2.625, end=2.875), # F
    # Bar 4: Bm7
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.0), # B
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.0), # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0), # F#
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0), # A
    # Bar 4: F7
    pretty_midi.Note(velocity=95, pitch=65, start=4.875, end=5.125), # F
    pretty_midi.Note(velocity=95, pitch=69, start=4.875, end=5.125), # A
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.125), # C
    pretty_midi.Note(velocity=95, pitch=72, start=4.875, end=5.125), # E
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75), # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write out the MIDI file
midi.write("dante_intro.mid")
