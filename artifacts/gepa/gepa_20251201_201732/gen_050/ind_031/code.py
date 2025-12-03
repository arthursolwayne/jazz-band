
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
]
for note in drums_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),   # A2
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),   # G2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),   # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),   # G2
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),  # A2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),   # F2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (Dm7): D, F, A, C
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),
    
    # Bar 3 (G7): G, B, D, F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),
    
    # Bar 4 (Cmaj7): C, E, G, B
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),
    
    # Bar 2 comp: 2 and 4
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),
    
    # Bar 3 comp: 2 and 4
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),
    
    # Bar 4 comp: 2 and 4
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),
    
    # Bar 4 resolution
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Saxophone motif
# One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),   # E4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),   # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # F#4
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),   # E4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),   # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),   # E4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),   # G4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # F#4
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),   # E4
    pretty_midi.Note(velocity=100, pitch=68, start=5.75, end=6.0),   # F#4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Fill in bar 2 and 4
# Bar 2 fill
drums_notes = [
    pretty_midi.Note(velocity=110, pitch=36, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=42, start=2.125, end=2.25),
]
for note in drums_notes:
    drums.notes.append(note)

# Bar 4 fill
drums_notes = [
    pretty_midi.Note(velocity=110, pitch=36, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=38, start=5.5, end=5.625),
    pretty_midi.Note(velocity=110, pitch=42, start=5.625, end=5.75),
]
for note in drums_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
