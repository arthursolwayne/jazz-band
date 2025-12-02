
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
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Eb, D, C, Bb, A, G, Ab)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=95, pitch=60, start=1.875, end=2.25),  # C7
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=95, pitch=57, start=3.375, end=3.75),  # Bb7
    pretty_midi.Note(velocity=95, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=95, pitch=64, start=4.875, end=5.25),  # F7
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=74, start=4.875, end=5.25),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax - short motif, make it sing
# Motif: F, Gb, Ab, C (Fm7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F (return)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 1.5)
    
# Add to drums
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("fm_intro.mid")
