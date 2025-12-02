
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

# Bass line: Marcus (F2 - Bb2, MIDI 53-57)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # F2
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),  # Bb2
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=90, pitch=56, start=4.125, end=4.5),  # A2
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),  # Bb2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (open voicings, different chord each bar, resolve on the last)
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25), # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25), # C5
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=2.25), # D5
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75), # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75), # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75), # Ab4
])
# Bar 4: Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25), # D5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.25), # A5
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25), # C5
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (one short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
# Motif: F4 - Eb4 - D4 - F4 (but start with F4, then delay the D4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625), # F4
    pretty_midi.Note(velocity=110, pitch=68, start=1.625, end=1.75), # Eb4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875), # D4
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),  # F4
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.125), # F4
    pretty_midi.Note(velocity=110, pitch=68, start=3.125, end=3.25), # Eb4
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375), # D4
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5),  # F4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
])
# Snare on 2 and 4
drum_notes.extend([
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
])
# Hi-hat on every eighth
drum_notes.extend([
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
])

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
