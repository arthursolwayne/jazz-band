
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
    # Hihat on every eighth
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

# Bass: Marcus - walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),   # G2
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),   # G2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),   # G2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 - D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25),  # C4
    # Bar 3 - G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75),  # F4
    # Bar 4 - Bm7 (B D F# A)
    pretty_midi.Note(velocity=90, pitch=73, start=4.5, end=5.25),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),  # D4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),  # A4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 - Start of motif
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # F#4
    # Bar 3 - Continue the motif, leave it hanging
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # F#4
    # Bar 4 - Come back and finish it
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),   # C5
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
