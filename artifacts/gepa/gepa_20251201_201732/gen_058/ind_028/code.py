
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

# Marcus: Walking bass line in Fm (F, Ab, D, C)
# Bar 2: F -> Ab -> D -> C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0), # C2
    # Bar 3: C -> F -> Ab -> D
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375), # C2
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5), # D2
    # Bar 4: D -> C -> F -> Ab
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.875), # D2
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25), # C2
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0), # Ab2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Piano chords, open voicings, each bar different, resolve on last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # D5
    # Bar 3: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # C4
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375), # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375), # Bb4
    # Bar 4: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # C5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # Eb5
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875), # G5
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Saxophone melody, one short motif, sing, start, leave it hanging, come back
# Motif: F, Ab, Bb, B (F4, Ab4, Bb4, B4) with a resolution on Bb4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # Ab4
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # B4
    # Come back and finish the motif
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875), # Bb4
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
