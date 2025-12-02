
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0),  # D#
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625), # A#
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),  # B
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25), # B
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75), # B
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=60, start=3.875, end=4.25), # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.875, end=4.25), # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.25), # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.875, end=4.25), # B
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25), # B
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - Short motif, sing it, make it hang
sax_notes = [
    # Bar 2 - motif starts
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),   # F
    # Bar 3 - leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5),   # F
    # Bar 4 - finish the motif
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.125),  # G#
    pretty_midi.Note(velocity=110, pitch=71, start=5.125, end=5.25),  # B
]
for note in sax_notes:
    sax.notes.append(note)

# Add tempo
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0,螃蟹=120)]
midi.tempo_changes = [pretty_midi.TempoChange(tempo=120, time=0.0)]

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
