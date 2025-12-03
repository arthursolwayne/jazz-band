
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hi-hat
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass (Walking line in Fm, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625), # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0), # Ab2
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375), # C3
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75), # D3
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125), # C#3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5), # D3
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875), # Bb2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625), # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0), # Ab2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane - Piano (Open voicings, resolve on the last chord)
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # C4 (duplicate for voicing)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # D4
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Ab4
]
# Bar 4: C7 (C, E, G, Bb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # C4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # E4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # G4 (duplicate for voicing)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # Bb4
]
# Bar 4: Resolution to Fm7 (F, Ab, C, D)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # D4
]
for note in piano_notes:
    piano.notes.append(note)

# Dante - Sax (Tenor sax, one short motif, make it sing)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875), # F3
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Ab3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # Ab3
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for Bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hi-hat
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare

    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hi-hat
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare

    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hi-hat
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
