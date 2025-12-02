
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=43, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=95, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=50, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=95, pitch=53, start=1.5, end=1.875),  # Bb7
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=43, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=95, pitch=48, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=95, pitch=50, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=95, pitch=53, start=3.0, end=3.375),  # Bb7
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=43, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=95, pitch=48, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=95, pitch=50, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=95, pitch=53, start=4.5, end=4.875),  # Bb7
]
piano.notes.extend(piano_notes)

# Sax: Dante - short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # Bb (Fm7)
    pretty_midi.Note(velocity=100, pitch=62, start=1.6875, end=1.875), # Ab
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # C#
    pretty_midi.Note(velocity=100, pitch=65, start=3.5625, end=3.75), # B
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.6875, end=4.875), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=5.0625, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.4375), # C#
    pretty_midi.Note(velocity=100, pitch=65, start=5.4375, end=5.625), # B
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125), # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=5.8125, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    kick3_start = start + 1.125
    kick3_end = kick3_start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick3_start, end=kick3_end))

    # Snare on 2 and 4
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    snare4_start = start + 1.875
    snare4_end = snare4_start + 0.125
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare4_start, end=snare4_end))

    # Hihat on every eighth
    for i in range(8):
        start_eighth = start + i * 0.1875
        end_eighth = start_eighth + 0.1875
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_eighth, end=end_eighth))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
