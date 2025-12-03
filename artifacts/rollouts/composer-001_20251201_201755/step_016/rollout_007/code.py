
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625), # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D (root)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # A (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D (root)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # D (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # Eb
]
# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # Ab
])
# Bar 4: F7 (F A C Eb) with resolution
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Eb
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F Ab Bb F (MIDI 64, 67, 69, 64)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # F (repeat)
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # F (repeat)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # F (repeat)
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # F (repeat)
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=6.0, end=6.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=6.0, end=6.25),  # F (end on F)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875))  # Wait, this is off
    # Fix snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on every eighth
    for i in range(0, 4):
        hihat_start = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
