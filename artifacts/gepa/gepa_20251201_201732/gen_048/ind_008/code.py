
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

# Marcus - Walking bass line in F (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0), # F2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375), # C3 (F root fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5), # C3
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625), # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0), # F2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E) -> F, A, C, E (MIDI 53, 58, 60, 64)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
]
# Bar 3: Bb7 (Bb, D, F, Ab) -> Bb, D, F, Ab (MIDI 50, 55, 60, 58)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),
])
# Bar 4: C7 (C, E, G, Bb) -> C, E, G, Bb (MIDI 60, 64, 67, 58)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),
])
for note in piano_notes:
    piano.notes.append(note)

# Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (60), A (65), Bb (62), F (60)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=2.0625, end=2.25), # F
    # Leave it hanging, come back and finish
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.8125, end=3.0),   # A
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
