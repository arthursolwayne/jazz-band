
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up instruments
# Tenor Sax (program 64)
tenor_sax = pretty_midi.Instrument(program=64)
pm.instruments.append(tenor_sax)

# Bass (program 33)
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# Piano (program 0)
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# Drums (program 10)
drums = pretty_midi.Instrument(program=10)
pm.instruments.append(drums)

# Define the tempo and time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, colon=True)]
pm.tempos = [pretty_midi.TempoChange(tempo=160.0, time=0.0)]

# Time per beat (in seconds) at 160 BPM
beat = 60.0 / 160.0
bar = beat * 4  # 4/4 time

# Define the time points for each bar
bar_times = [0.0, bar, bar * 2, bar * 3, bar * 4]

# == DRUMS: Bar 1 - Just kick and snare on 1 and 3 ==
# Little Ray: Kick on 1, snare on 3, hihat on every eighth
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=bar_times[0], end=bar_times[0] + 0.1)
snare_note = pretty_midi.Note(velocity=80, pitch=38, start=bar_times[0] + beat * 2, end=bar_times[0] + beat * 2 + 0.1)
hihat_notes = [pretty_midi.Note(velocity=80, pitch=42, start=bar_times[0] + i * beat / 2, end=bar_times[0] + i * beat / 2 + 0.05) for i in range(8)]

drums.notes.extend([kick_note, snare_note] + hihat_notes)

# == BASS: Bar 1 - Walking line in F ==
# Marcus: Walking line in F, chromatic approaches

# F7 chord: F, A, C, E
# Walking bass line: F -> Ab -> Bb -> C -> E -> G -> A -> Bb -> F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=bar_times[0], end=bar_times[0] + 0.3),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=bar_times[0] + beat, end=bar_times[0] + beat + 0.3),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=bar_times[0] + beat * 2, end=bar_times[0] + beat * 2 + 0.3),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=bar_times[0] + beat * 3, end=bar_times[0] + beat * 3 + 0.3),  # C
]

bass.notes.extend(bass_notes)

# == PIANO: Bar 1 - Rest ==
# Diane: No piano in first bar, building anticipation

# == TENOR SAX: Bar 1 - Rest ==
# You: No sax, waiting for the moment

# == DRUMS: Bar 2 - Kick on 1, snare on 3, hihat on every eighth ==
# Little Ray: Same pattern as Bar 1
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=bar_times[1], end=bar_times[1] + 0.1)
snare_note = pretty_midi.Note(velocity=80, pitch=38, start=bar_times[1] + beat * 2, end=bar_times[1] + beat * 2 + 0.1)
hihat_notes = [pretty_midi.Note(velocity=80, pitch=42, start=bar_times[1] + i * beat / 2, end=bar_times[1] + i * beat / 2 + 0.05) for i in range(8)]

drums.notes.extend([kick_note, snare_note] + hihat_notes)

# == BASS: Bar 2 - Walking line in F7 ==
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=74, start=bar_times[1], end=bar_times[1] + 0.3),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=bar_times[1] + beat, end=bar_times[1] + beat + 0.3),  # G
    pretty_midi.Note(velocity=80, pitch=77, start=bar_times[1] + beat * 2, end=bar_times[1] + beat * 2 + 0.3),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar_times[1] + beat * 3, end=bar_times[1] + beat * 3 + 0.3),  # Bb
]

bass.notes.extend(bass_notes)

# == PIANO: Bar 2 - Diane plays F7 on beats 2 and 4 ==
# Diane: 7th chords on 2 and 4
# F7 = F, A, C, E

# F on beat 2 (time = bar_times[1] + beat)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=bar_times[1] + beat, end=bar_times[1] + beat + 0.25),
    pretty_midi.Note(velocity=90, pitch=74, start=bar_times[1] + beat, end=bar_times[1] + beat + 0.25),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=bar_times[1] + beat, end=bar_times[1] + beat + 0.25),  # G
    pretty_midi.Note(velocity=90, pitch=78, start=bar_times[1] + beat, end=bar_times[1] + beat + 0.25),  # A

    pretty_midi.Note(velocity=90, pitch=71, start=bar_times[1] + beat * 3, end=bar_times[1] + beat * 3 + 0.25),
    pretty_midi.Note(velocity=90, pitch=74, start=bar_times[1] + beat * 3, end=bar_times[1] + beat * 3 + 0.25),
    pretty_midi.Note(velocity=90, pitch=76, start=bar_times[1] + beat * 3, end=bar_times[1] + beat * 3 + 0.25),
    pretty_midi.Note(velocity=90, pitch=78, start=bar_times[1] + beat * 3, end=bar_times[1] + beat * 3 + 0.25),
]

piano.notes.extend(piano_notes)

# == TENOR SAX: Bar 2 - Start of your motif ==
# You: One short motif — F, Ab, Bb, C (F7 arpeggio), but with space and dynamics

# F (71)
note1 = pretty_midi.Note(velocity=100, pitch=71, start=bar_times[1], end=bar_times[1] + 0.4)
# Ab (68)
note2 = pretty_midi.Note(velocity=90, pitch=68, start=bar_times[1] + 0.5, end=bar_times[1] + 0.9)
# Bb (71)
note3 = pretty_midi.Note(velocity=100, pitch=71, start=bar_times[1] + 1.1, end=bar_times[1] + 1.5)
# C (72) — but leave it hanging
note4 = pretty_midi.Note(velocity=100, pitch=72, start=bar_times[1] + 1.6, end=bar_times[1] + 1.9)

tenor_sax.notes.extend([note1, note2, note3, note4])

# == DRUMS: Bar 3 - Kick on 1, snare on 3, hihat on every eighth ==
# Little Ray: Same pattern as Bar 1
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=bar_times[2], end=bar_times[2] + 0.1)
snare_note = pretty_midi.Note(velocity=80, pitch=38, start=bar_times[2] + beat * 2, end=bar_times[2] + beat * 2 + 0.1)
hihat_notes = [pretty_midi.Note(velocity=80, pitch=42, start=bar_times[2] + i * beat / 2, end=bar_times[2] + i * beat / 2 + 0.05) for i in range(8)]

drums.notes.extend([kick_note, snare_note] + hihat_notes)

# == BASS: Bar 3 - Walking line in F7 ==
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=bar_times[2], end=bar_times[2] + 0.3),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=bar_times[2] + beat, end=bar_times[2] + beat + 0.3),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=bar_times[2] + beat * 2, end=bar_times[2] + beat * 2 + 0.3),  # G
    pretty_midi.Note(velocity=80, pitch=77, start=bar_times[2] + beat * 3, end=bar_times[2] + beat * 3 + 0.3),  # A
]

bass.notes.extend(bass_notes)

# == PIANO: Bar 3 - Diane plays F7 on beats 2 and 4 ==
# Diane: 7th chords on 2 and 4 — same as Bar 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=bar_times[2] + beat, end=bar_times[2] + beat + 0.25),
    pretty_midi.Note(velocity=90, pitch=74, start=bar_times[2] + beat, end=bar_times[2] + beat + 0.25),
    pretty_midi.Note(velocity=90, pitch=76, start=bar_times[2] + beat, end=bar_times[2] + beat + 0.25),
    pretty_midi.Note(velocity=90, pitch=78, start=bar_times[2] + beat, end=bar_times[2] + beat + 0.25),

    pretty_midi.Note(velocity=90, pitch=71, start=bar_times[2] + beat * 3, end=bar_times[2] + beat * 3 + 0.25),
    pretty_midi.Note(velocity=90, pitch=74, start=bar_times[2] + beat * 3, end=bar_times[2] + beat * 3 + 0.25),
    pretty_midi.Note(velocity=90, pitch=76, start=bar_times[2] + beat * 3, end=bar_times[2] + beat * 3 + 0.25),
    pretty_midi.Note(velocity=90, pitch=78, start=bar_times[2] + beat * 3, end=bar_times[2] + beat * 3 + 0.25),
]

piano.notes.extend(piano_notes)

# == TENOR SAX: Bar 3 - Motif repeats with slight variation ==
# You: Repeat the motif with slightly different dynamics and timing to build tension

note1 = pretty_midi.Note(velocity=105, pitch=71, start=bar_times[2], end=bar_times[2] + 0.4)
note2 = pretty_midi.Note(velocity=95, pitch=68, start=bar_times[2] + 0.5, end=bar_times[2] + 0.9)
note3 = pretty_midi.Note(velocity=105, pitch=71, start=bar_times[2] + 1.1, end=bar_times[2] + 1.5)
note4 = pretty_midi.Note(velocity=105, pitch=72, start=bar_times[2] + 1.6, end=bar_times[2] + 1.9)

tenor_sax.notes.extend([note1, note2, note3, note4])

# == DRUMS: Bar 4 - Kick on 1, snare on 3, hihat on every eighth ==
# Little Ray: Same pattern as Bar 1
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=bar_times[3], end=bar_times[3] + 0.1)
snare_note = pretty_midi.Note(velocity=80, pitch=38, start=bar_times[3] + beat * 2, end=bar_times[3] + beat * 2 + 0.1)
hihat_notes = [pretty_midi.Note(velocity=80, pitch=42, start=bar_times[3] + i * beat / 2, end=bar_times[3] + i * beat / 2 + 0.05) for i in range(8)]

drums.notes.extend([kick_note, snare_note] + hihat_notes)

# == BASS: Bar 4 - Walking line in F7 ==
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=78, start=bar_times[3], end=bar_times[3] + 0.3),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar_times[3] + beat, end=bar_times[3] + beat + 0.3),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=bar_times[3] + beat * 2, end=bar_times[3] + beat * 2 + 0.3),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=bar_times[3] + beat * 3, end=bar_times[3] + beat * 3 + 0.3),  # F
]

bass.notes.extend(bass_notes)

# == PIANO: Bar 4 - Diane plays F7 on beats 2 and 4 ==
# Diane: 7th chords on 2 and 4 — same as Bar 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=bar_times[3] + beat, end=bar_times[3] + beat + 0.25),
    pretty_midi.Note(velocity=90, pitch=74, start=bar_times[3] + beat, end=bar_times[3] + beat + 0.25),
    pretty_midi.Note(velocity=90, pitch=76, start=bar_times[3] + beat, end=bar_times[3] + beat + 0.25),
    pretty_midi.Note(velocity=90, pitch=78, start=bar_times[3] + beat, end=bar_times[3] + beat + 0.25),

    pretty_midi.Note(velocity=90, pitch=71, start=bar_times[3] + beat * 3, end=bar_times[3] + beat * 3 + 0.25),
    pretty_midi.Note(velocity=90, pitch=74, start=bar_times[3] + beat * 3, end=bar_times[3] + beat * 3 + 0.25),
    pretty_midi.Note(velocity=90, pitch=76, start=bar_times[3] + beat * 3, end=bar_times[3] + beat * 3 + 0.25),
    pretty_midi.Note(velocity=90, pitch=78, start=bar_times[3] + beat * 3, end=bar_times[3] + beat * 3 + 0.25),
]

piano.notes.extend(piano_notes)

# == TENOR SAX: Bar 4 - Finish the motif with a full resolution ==
# You: Complete the motif, resolve to C with a little flourish

note1 = pretty_midi.Note(velocity=100, pitch=71, start=bar_times[3], end=bar_times[3] + 0.4)
note2 = pretty_midi.Note(velocity=90, pitch=68, start=bar_times[3] + 0.5, end=bar_times[3] + 0.9)
note3 = pretty_midi.Note(velocity=100, pitch=71, start=bar_times[3] + 1.1, end=bar_times[3] + 1.5)
note4 = pretty_midi.Note(velocity=100, pitch=72, start=bar_times[3] + 1.6, end=bar_times[3] + 1.9)

# Add a small flourish at the end
flourish = pretty_midi.Note(velocity=110, pitch=74, start=bar_times[3] + 1.9, end=bar_times[3] + 2.0)

tenor_sax.notes.extend([note1, note2, note3, note4, flourish])

# Save the MIDI file
pm.write("f_intro.mid")
