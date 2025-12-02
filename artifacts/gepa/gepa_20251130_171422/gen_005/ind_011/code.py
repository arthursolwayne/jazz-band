
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick (36), snare (38), hihat (42)
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Set the key: Dm (D minor)
# Scale degrees: D, Eb, F, G, Ab, Bb, C
# Tonic: D (62)
# Scale: Dm7 is D, F, Ab, C

# Define note durations and time
beat = 0.375  # 60 / 160
bar = 1.5     # 4 beats per bar

# Bar 1: Little Ray (Drums) only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for beat_index in range(4):
    time = beat_index * beat
    if beat_index % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + beat)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + beat)
        drums.notes.append(note)
    # Hihat on every 8th
    for eighth in [0, 0.1875, 0.375, 0.5625]:
        note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time + eighth, end=time + eighth + 0.1875)
        drums.notes.append(note)

# Bar 2: Full Quartet (1.5 - 3.0s)
# SAX: Motif starts here, a single line that lingers
# D to F to Ab to C in 8th notes with a rest halfway
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0)   # D (repeat, slightly delayed)
]
sax.notes.extend(sax_notes)

# BASS: Walking line with chromatic approach
# Dm7: D, F, Ab, C
# Chromatic approaches to each chord tone
bass_notes = [
    pretty_midi.Note(velocity=75, pitch=62, start=1.5, end=1.5 + beat),   # D
    pretty_midi.Note(velocity=75, pitch=63, start=1.5 + beat, end=1.5 + 2 * beat),  # Eb (approach to F)
    pretty_midi.Note(velocity=75, pitch=64, start=1.5 + 2 * beat, end=1.5 + 3 * beat),  # F
    pretty_midi.Note(velocity=75, pitch=66, start=1.5 + 3 * beat, end=1.5 + 4 * beat),  # G (approach to Ab)
    pretty_midi.Note(velocity=75, pitch=67, start=1.5 + 4 * beat, end=1.5 + 5 * beat),  # Ab
    pretty_midi.Note(velocity=75, pitch=68, start=1.5 + 5 * beat, end=1.5 + 6 * beat),  # A (approach to Bb)
    pretty_midi.Note(velocity=75, pitch=69, start=1.5 + 6 * beat, end=1.5 + 7 * beat),  # Bb
    pretty_midi.Note(velocity=75, pitch=71, start=1.5 + 7 * beat, end=1.5 + 8 * beat),  # C
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords, comp on 2 and 4
# Dm7: D, F, Ab, C
# Root position on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5 + beat, end=1.5 + beat + 0.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5 + beat, end=1.5 + beat + 0.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + beat, end=1.5 + beat + 0.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=1.5 + beat, end=1.5 + beat + 0.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 3 * beat, end=1.5 + 3 * beat + 0.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5 + 3 * beat, end=1.5 + 3 * beat + 0.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 3 * beat, end=1.5 + 3 * beat + 0.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=1.5 + 3 * beat, end=1.5 + 3 * beat + 0.25),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full Quartet (3.0 - 4.5s)
# SAX: Same motif, but shifted up a half step
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5)   # Eb (repeat, slightly delayed)
]
sax.notes.extend(sax_notes)

# BASS: Keep the walking line
bass_notes = [
    pretty_midi.Note(velocity=75, pitch=64, start=3.0, end=3.0 + beat),   # Eb
    pretty_midi.Note(velocity=75, pitch=65, start=3.0 + beat, end=3.0 + 2 * beat),  # F#
    pretty_midi.Note(velocity=75, pitch=66, start=3.0 + 2 * beat, end=3.0 + 3 * beat),  # G
    pretty_midi.Note(velocity=75, pitch=68, start=3.0 + 3 * beat, end=3.0 + 4 * beat),  # A
    pretty_midi.Note(velocity=75, pitch=69, start=3.0 + 4 * beat, end=3.0 + 5 * beat),  # Bb
    pretty_midi.Note(velocity=75, pitch=70, start=3.0 + 5 * beat, end=3.0 + 6 * beat),  # B
    pretty_midi.Note(velocity=75, pitch=71, start=3.0 + 6 * beat, end=3.0 + 7 * beat),  # C
    pretty_midi.Note(velocity=75, pitch=72, start=3.0 + 7 * beat, end=3.0 + 8 * beat),  # D
]
bass.notes.extend(bass_notes)

# PIANO: Comp again on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0 + beat, end=3.0 + beat + 0.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=66, start=3.0 + beat, end=3.0 + beat + 0.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0 + beat, end=3.0 + beat + 0.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.0 + beat, end=3.0 + beat + 0.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.0 + 3 * beat, end=3.0 + 3 * beat + 0.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=66, start=3.0 + 3 * beat, end=3.0 + 3 * beat + 0.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0 + 3 * beat, end=3.0 + 3 * beat + 0.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.0 + 3 * beat, end=3.0 + 3 * beat + 0.25),  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full Quartet (4.5 - 6.0s)
# SAX: Same motif, but back to D minor, with a rest before the last note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75)   # C (after a rest)
]
sax.notes.extend(sax_notes)

# BASS: Complete the walking line
bass_notes = [
    pretty_midi.Note(velocity=75, pitch=62, start=4.5, end=4.5 + beat),   # D
    pretty_midi.Note(velocity=75, pitch=63, start=4.5 + beat, end=4.5 + 2 * beat),  # Eb
    pretty_midi.Note(velocity=75, pitch=64, start=4.5 + 2 * beat, end=4.5 + 3 * beat),  # F
    pretty_midi.Note(velocity=75, pitch=66, start=4.5 + 3 * beat, end=4.5 + 4 * beat),  # G
    pretty_midi.Note(velocity=75, pitch=67, start=4.5 + 4 * beat, end=4.5 + 5 * beat),  # Ab
    pretty_midi.Note(velocity=75, pitch=68, start=4.5 + 5 * beat, end=4.5 + 6 * beat),  # A
    pretty_midi.Note(velocity=75, pitch=69, start=4.5 + 6 * beat, end=4.5 + 7 * beat),  # Bb
    pretty_midi.Note(velocity=75, pitch=71, start=4.5 + 7 * beat, end=4.5 + 8 * beat),  # C
]
bass.notes.extend(bass_notes)

# PIANO: Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5 + beat, end=4.5 + beat + 0.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5 + beat, end=4.5 + beat + 0.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5 + beat, end=4.5 + beat + 0.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.5 + beat, end=4.5 + beat + 0.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5 + 3 * beat, end=4.5 + 3 * beat + 0.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5 + 3 * beat, end=4.5 + 3 * beat + 0.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5 + 3 * beat, end=4.5 + 3 * beat + 0.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.5 + 3 * beat, end=4.5 + 3 * beat + 0.25),  # C
]
piano.notes.extend(piano_notes)

# Add drums for the final bar (4.5 - 6.0s)
for beat_index in range(4):
    time = 4.5 + beat_index * beat
    if beat_index % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + beat)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + beat)
        drums.notes.append(note)
    # Hihat on every 8th
    for eighth in [0, 0.1875, 0.375, 0.5625]:
        note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time + eighth, end=time + eighth + 0.1875)
        drums.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
