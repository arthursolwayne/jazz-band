
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - 7th chord on 2 (Bb7)
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=85, pitch=77, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=80, start=1.875, end=2.25), # G
    # Bar 2 - 7th chord on 4 (F7)
    pretty_midi.Note(velocity=95, pitch=64, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=85, pitch=69, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0), # D
    # Bar 3 - 7th chord on 2 (Eb7)
    pretty_midi.Note(velocity=95, pitch=60, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=85, pitch=65, start=3.375, end=3.75), # G#
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # Bb
    # Bar 3 - 7th chord on 4 (Ab7)
    pretty_midi.Note(velocity=95, pitch=57, start=4.125, end=4.5), # Ab
    pretty_midi.Note(velocity=90, pitch=61, start=4.125, end=4.5), # C
    pretty_midi.Note(velocity=85, pitch=62, start=4.125, end=4.5), # C#
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5), # Eb
    # Bar 4 - 7th chord on 2 (Bb7)
    pretty_midi.Note(velocity=95, pitch=72, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=85, pitch=77, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=80, start=4.875, end=5.25), # G
    # Bar 4 - 7th chord on 4 (F7)
    pretty_midi.Note(velocity=95, pitch=64, start=5.625, end=6.0), # F
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0), # A
    pretty_midi.Note(velocity=85, pitch=69, start=5.625, end=6.0), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0), # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # A
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875), # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=110, pitch=69, start=3.5625, end=3.75), # B
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.4375), # A
    pretty_midi.Note(velocity=110, pitch=64, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.8125), # D
    pretty_midi.Note(velocity=110, pitch=60, start=5.8125, end=6.0), # C
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),   # Snare 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.9375), # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.625), # Kick 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),   # Snare 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.4375), # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.9375), # Kick 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),   # Snare 4
]
# Hihat on every eighth note from 1.5 to 6.0
for i in range(12):
    start = 1.5 + i * 0.375
    end = start + 0.1875
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
