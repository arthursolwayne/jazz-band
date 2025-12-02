
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # F -> Gb -> G -> A (F7 chord)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0), # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5), # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25), # Bb
    # F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0), # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
sax_notes = [
    # Start with a short motif: F -> Bb -> G -> F
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0), # F
    # End on a suspended note
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25), # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Chromatic approach to Bb
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25), # G
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5), # G#
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0), # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75), # F
    # Bb7 on beat 4
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5), # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=4.25, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5), # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5), # F
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, resolve on Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.125), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25), # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.375), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5), # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.625), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75), # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25), # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75), # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=5.0), # A#
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5), # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25), # Bb
    # F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0), # F
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0), # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0), # Bb
]
piano.notes.extend(piano_notes)

# Sax: Resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.625), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75), # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=4.875), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0), # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.125), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.25), # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75), # F
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
]
drums.notes.extend(drum_notes)

# Add hi-hat on every eighth
for i in range(16):
    start = i * 0.375
    end = start + 0.1875
    if end <= 6.0:
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
