
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

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75), # Db
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=80, pitch=58, start=4.125, end=4.5), # F
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=61, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0), # C
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25), # F
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75), # Ab
    # Bar 4: Eb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25), # D
]
piano.notes.extend(piano_notes)

# Saxophone (Dante) - short motif, start it, leave it hanging, come back
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0), # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25), # B
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5), # A
    pretty_midi.Note(velocity=110, pitch=68, start=2.5, end=2.75), # G
    pretty_midi.Note(velocity=110, pitch=66, start=2.75, end=3.0), # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25), # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5), # B
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75), # A
    pretty_midi.Note(velocity=110, pitch=68, start=3.75, end=4.0), # G
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25), # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.5), # A
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75), # B
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0), # A
    pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.25), # F
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.5), # G
    pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.75), # F
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0), # A
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375), # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick 3
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875), # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375), # Kick 3
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375), # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875), # Kick 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125), # Snare 4
]
for note in drum_notes:
    drums.notes.append(note)

# Add hi-hats every eighth note from 1.5s to 6.0s
for i in range(int((6.0 - 1.5) / 0.1875)):
    start = 1.5 + i * 0.1875
    end = start + 0.1875
    if end > 6.0:
        end = 6.0
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
