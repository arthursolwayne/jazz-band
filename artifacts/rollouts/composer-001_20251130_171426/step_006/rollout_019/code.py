
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches
bass_notes = [
    # Bar 2: Dm7 (D, F, A, C) walking line
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # D#
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
    # Bar 3: Chromatic approach to G
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # F#
    # Bar 4: Chromatic approach to C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # C
    # Bar 3: Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # C
    # Bar 4: G7 on beat 2
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # C#
    # Bar 4: Cm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=60, start=6.0, end=6.375), # C
    pretty_midi.Note(velocity=100, pitch=65, start=6.0, end=6.375), # E
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=6.0, end=6.375), # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # G (chromatic)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A (tension)
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # Bb (resolve)
    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # B (resolution)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # F
    # Let the motif breathe
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Add the drums to the instrument
drums.notes.extend(drum_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
