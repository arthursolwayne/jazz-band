
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # D (root)
    pretty_midi.Note(velocity=100, pitch=56, start=1.875, end=2.25), # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # E (3rd)
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # G (5th)
    
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # A (6th)
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75), # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # B (7th)
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # D (octave)
    
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25), # E (3rd)
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625), # G (5th)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # A (6th)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A7
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A7
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # A7
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (66), G (67), D (62) — but with a twist
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375),  # D (come back)
    pretty_midi.Note(velocity=110, pitch=66, start=2.375, end=2.5),  # F#
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=2.875),  # Bb (chromatic)
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Full in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25),
    
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 2.625, end=bar_start + 3.0),

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
